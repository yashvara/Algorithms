def weighted_job_scheduling(jobs, processing_time_limit):

    # Sort the jobs in decreasing order of weight.
    jobs.sort(key=lambda job: job[0], reverse=True)

    # Initialize the total weight and the current time.
    total_weight = 0
    current_time = 0

    for job in jobs:
        if current_time + job[1] <= processing_time_limit:
            total_weight += job[0]
            current_time += job[1]
    return total_weight

jobs = [(10, 2), (5, 1), (3, 3)]
processing_time_limit = 5
max_total_weight = weighted_job_scheduling(jobs, processing_time_limit)
print(max_total_weight)


