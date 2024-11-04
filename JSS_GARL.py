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
    makespan = max(sch[-1][1][1] for sch in schedule)
    return makespan


def display(schedule, makespan):
    print(f"The makespan of the optimal solution is: {makespan}")
    output = ""
    for mac in range(len(schedule)):
        output += f"Machine {mac}: "
        for op in schedule[mac]:
            job = op[0][0]
            task = op[0][1]
            output += f"\tJob_{job} task{ task}"
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
         [(0, 3), (1, 2), (2, 2), (3, 4)],  # Job0
        [(0, 2), (2, 1), (1, 4)],  # Job1
        [(1, 4), (2, 3)],  # Job2
        [(2, 2), (0, 1), (3, 3), (1, 2)]    # Job3
    ]

    population_size = 10
    population = [create_schedule(jobs_data) for _ in range (population_size)]

    fitness_scores = [fitness_function(schedule) for schedule in population]

    idx = fitness_scores.index(min(fitness_scores))
    makespan = fitness_scores[idx]
    schedule = population[idx]

    display(schedule, makespan)


if __name__ == "__main__":
    main()