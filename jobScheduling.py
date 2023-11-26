def jobScheduling(jobs, d, n):
    job_seq = ['-1'] * d
    index = list(range(n))
    index.sort(key=lambda i: jobs[i][2], reverse=True)
    
    for i in index:
        for j in range(jobs[i][1] - 1, -1, -1):
            if job_seq[j] == '-1':
                job_seq[j] = jobs[i][0]
                break

    print(job_seq)

jobs = [['a', 2, 15], ['b', 1, 13], ['c', 2, 17], ['d', 2, 18], ['e', 3, 12], ['f', 3, 14]]
n = len(jobs)
deadline = [jobs[i][1] for i in range(n)]
d = max(deadline)

jobScheduling(jobs, d, n)

