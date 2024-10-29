import random
from collections import deque

"""Minimal Job Shop Problem"""
def main() -> None:
    jobs_data = [  # task = (machine_id, processing_time).
        [(0, 3), (1, 2), (2, 2)],  # Job0
        [(0, 2), (2, 1), (1, 4)],  # Job1
        [(1, 4), (2, 3)],  # Job2
    ]

    machine_count = 1 + max(task[0] for job in jobs_data for task in job)
    job_count = len(jobs_data)
    job_queues = [deque(job) for job in jobs_data]
    job_endtime = [0 for _ in jobs_data]    # Will give the possible start time.
    schedule = [deque() for _ in range(machine_count)]
    print(schedule)
    while any(queue for queue in job_queues):   # Continue while any queue is not empty.
        job = random.randint(0,job_count-1)
        if job_queues[job]: # Check if the specific queue is not empty.
            task = job_queues[job].popleft()
            start_time = job_endtime[job]


if __name__ == "__main__":
    main()