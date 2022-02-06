def get_shortest_job(ready_jobs):
    counter = float('inf')
    result = None

    for job, remainder in ready_jobs.items():
        if counter > remainder:
            result = job
            counter = remainder

    return result




def shortestJobRemaining(interrupts, jobs):
    ready_list = {}
    result = [None] * sum(jobs.values())
    job_completion = {}
    index = 0

    while index < len(result):

        if index in interrupts:
            jobs_interrupt = interrupts[index]
            for job in jobs_interrupt:
                ready_list[job] = jobs[job]
        shortest_job = get_shortest_job(ready_list)
        try:
            ready_list[shortest_job] = ready_list[shortest_job] - 1
        except:
            import pdb; pdb.set_trace()
        result[index] = shortest_job
        if ready_list[shortest_job] == 0:
            job_completion[shortest_job] = index + 1
            del ready_list[shortest_job]
        index += 1
    return result, job_completion