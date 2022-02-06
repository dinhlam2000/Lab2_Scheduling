def fifo(interrupts, jobs):
    result = []
    job_completion = {}
    counter = 0
    for interrupt, value in interrupts.items():
        for job in value:
            burst_time = jobs[job]
            result = result + [job] * burst_time
            job_completion[job] = counter + burst_time
            counter = counter + burst_time
    return result, job_completion
    pass