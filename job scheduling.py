def job_scheduling(jobs):
    # Sort jobs in descending order of their profits
    jobs.sort(key=lambda x: x[2], reverse=True)
    n = len(jobs)
    result = [-1] * n
    slots = [False] * n

    # Iterate over each job
    for i in range(n):
        # Find a free slot starting from the end
        for j in range(min(n, jobs[i][1]) - 1, -1, -1):
            if not slots[j]:
                slots[j] = True
                result[j] = jobs[i][0]
                break

    return result


# Example usage:
# Each job is represented as a tuple (job_id, deadline, profit)
jobs = [
    (1, 4, 70),
    (2, 1, 80),
    (3, 2, 50),
    (4, 1, 10),
    (5, 3, 60),
]
scheduled_jobs = job_scheduling(jobs)
print("Scheduled Jobs:", scheduled_jobs)
