"""Minimal Job Shop Problem"""
def main() -> None:
    jobs_data = [  # task = (machine_id, processing_time).
        [(0, 3), (1, 2), (2, 2)],  # Job0
        [(0, 2), (2, 1), (1, 4)],  # Job1
        [(1, 4), (2, 3)],  # Job2
    ]

    machine_count = 1 + max(task[0] for job in jobs_data for task in job)
    all_machines = range(machine_count)


if __name__ == "__main__":
    main()