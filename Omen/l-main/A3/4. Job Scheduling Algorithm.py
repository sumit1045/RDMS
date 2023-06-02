def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[1])  # Sort jobs by their deadlines
    schedule = []
    max_deadline = max(jobs, key=lambda x: x[1])[1]

    time_slots = [False] * (max_deadline + 1)

    for job in jobs:
        deadline = job[1]
        while deadline > 0:
            if time_slots[deadline] == False:
                time_slots[deadline] = True
                schedule.append(job)
                break
            deadline -= 1

    return schedule

# Example jobs [job_id, deadline, profit]
jobs = [[1, 2, 100], [2, 1, 50], [3, 2, 200], [4, 3, 300], [5, 1, 25]]

schedule = job_scheduling(jobs)

print("Scheduled jobs:")
for job in schedule:
    print(f"Job {job[0]} with deadline {job[1]} and profit {job[2]}")
