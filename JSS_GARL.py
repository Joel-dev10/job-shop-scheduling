import random
from collections import deque

"""Minimal Job Shop Problem"""

def create_schedule(jobs_data):
    machine_count = 1 + max(task[0] for job in jobs_data for task in job)
    job_count = len(jobs_data)
    job_queues = [deque(job) for job in jobs_data]
    job_details = [[0,0] for _ in jobs_data]    # Will give the possible start time and task counter.
    schedule = [deque() for _ in range(machine_count)]  # Should contain [(job,task),[start_time,end_time]]
    while any(queue for queue in job_queues):   # Continue while any queue is not empty.
        job = random.randint(0,job_count-1)
        if job_queues[job]: # Check if the specific queue is not empty.
            task = job_queues[job].popleft()    # Task[0] gives machine_id and task[1] gives duration.
            start_time = job_details[job][0]
            if schedule[task[0]]:   # To check if machine is used.
                machine_endtime = schedule[task[0]][-1][1][1]
                if machine_endtime > start_time:
                    start_time = machine_endtime
            schedule[task[0]].append([(job, job_details[job][1]),[start_time, start_time + task[1]]])
            job_details[job][0] = start_time + task[1]
            job_details[job][1] += 1 
    return schedule


def fitness_function(schedule):
    # 100 is taken as makespan presently does not go over than 100 units.
    score = 100/max(sch[-1][1][1] for sch in schedule)
    return score


def crossover(parent1, parent2, machine_count):
    crosspoint = random.randint(0, machine_count-1)
    child1 = parent1[:crosspoint] + parent2[crosspoint:]
    child2 = parent2[crosspoint:] + parent1[:crosspoint]
    return child1, child2


def mutate(child, machine_count):
    # Scramble Mutation is implemented for a single machine.
    machine = random.randint(0, machine_count-1)
    random.shuffle(child[machine])
    return child
    


def add(temp_sch, job_start, machine_start, jobs_data, job, task):
    if task == 0 or (job, task-1) in [col[0] for row in temp_sch for col in row]:
        machine = jobs_data[job][task][0]
        duration = jobs_data[job][task][1]
        start = max(machine_start[machine], job_start[job])
        temp_sch[machine].append([(job, task), [start, start+duration]])
        machine_start[machine] = start + duration
        job_start[job] = start + duration
        return temp_sch, job_start, machine_start
    else:
        temp_sch, job_start, machine_start = add(temp_sch, job_start, machine_start, jobs_data, job, task-1)
        machine = jobs_data[job][task][0]
        duration = jobs_data[job][task][1]
        start = max(machine_start[machine], job_start[job])
        temp_sch[machine].append([(job, task), [start, start+duration]])
        machine_start[machine] = start + duration
        job_start[job] = start + duration
        return temp_sch, job_start, machine_start


def correction(schedule, jobs_data):
    # Correcting now according to the task list of the first machine. In future can be done according to machine priority.
    job_start = [0 for _ in jobs_data]
    machine_start = [0 for _ in schedule]
    temp_sch = [deque() for _ in schedule]
    for sch in schedule:
        for op in sch:             
            while op[0] not in [col[0] for row in temp_sch for col in row]:
                job = op[0][0]
                task = op[0][1]
                temp_sch, job_start, machine_start = add(temp_sch, job_start, machine_start, jobs_data, job, task)
    return temp_sch


def display(schedule, makespan):
    print(f"The makespan of the optimal solution is: {makespan}")
    output = ""
    for mac in range(len(schedule)):
        output += f"Machine {mac}: "
        for op in schedule[mac]:
            job = op[0][0]
            task = op[0][1]
            output += f"\tJob_{job} task_{task}"
        output += "\n\t\t"
        for op in schedule[mac]:
            time = op[1]
            if len(str(time)) < 8:
                output += f"{time}\t\t"
            else:
                output += f"{time}\t"
        output += "\n"
    print(output)
                

def main() -> None:

    jobs_data = [  # task = (machine_id, processing_time).
        [(0, 3), (1, 2), (2, 2), (3, 4)],   # Job0
        [(0, 2), (2, 1), (1, 4)],   # Job1
        [(1, 4), (2, 3)],   # Job2
        [(2, 2), (0, 1), (3, 3), (1, 2)]    # Job3
    ]

    machine_count = 1 + max(task[0] for job in jobs_data for task in job)

    population_size = 10
    generation_size = 50

    population = [create_schedule(jobs_data) for _ in range (population_size)]
    fitness_scores = [fitness_function(schedule) for schedule in population]

    for generation in range(generation_size):
        next_population = []
        temp_pop = [x for x, _ in sorted(zip(population, fitness_scores), key = lambda pair: pair[1], reverse = True)[:8]]
        next_population.append(temp_pop[0])
        next_population.append(temp_pop[1])
        
        while len(next_population) < population_size:
            parent1 = random.choice(temp_pop)
            parent2 = random.choice(temp_pop)
            child1, child2 = crossover(parent1, parent2, machine_count)
            if random.random() < 0.1:
                child1 = mutate(child1, machine_count)
            if random.random() < 0.1:
                child2 = mutate(child2, machine_count)
            child1 = correction(child1, jobs_data)
            child2 = correction(child2, jobs_data)
            next_population.append(child1)
            next_population.append(child2)

        population = next_population
        fitness_scores = [fitness_function(schedule) for schedule in population]

    idx = fitness_scores.index(max(fitness_scores))
    makespan = max(sch[-1][1][1] for sch in population[idx])
    schedule = population[idx]

    display(schedule, makespan)


if __name__ == "__main__":
    main()