import sys


# looking at head of queue
# pop up the first one in the list --> current_process
# fill list with current_process q times
# based on the time -->
# if there is an interrupt: (inclusive from both endpoints of current process)
# add new process to the queue
# if current_process is exhausted:
# fill in with the next one on the queue
# case 1: if on the batch that has an interrupt
#       -> put that value onto the batch but do
def roundrobin(interrupts, jobs, q):

    queue = interrupts[0] #start a queue that holds all the values that arrives at 0 in the order of highest priority

    result = [None] * (sum(jobs.values()))  #have a result list that has a length of all processes

    job_completion = {}

    #now fill that result list starting at the beginning all the way til end
    counter = 0
    while counter < len(result):
        interrupts_queue = []
        i = 0
        current_process = queue.pop(0)
        while i < q:
            if jobs[current_process] <= 0: #meaning the current process has exhausted so we move onto the process on the top of the queue
                break

            jobs[current_process] = jobs[current_process] - 1
            result[counter] = current_process
            counter += 1
            i += 1
            if counter in interrupts and q == 1:
                interrupts_queue = interrupts_queue + interrupts[counter]
            elif counter in interrupts and q > 1:
                queue = queue + interrupts[counter]

        queue = interrupts_queue + queue

        if jobs[current_process] > 0:
            queue = queue + [current_process] #add the current process that was just executed toward the end of the queue now for round robin
        else:
            job_completion[current_process] = counter

    return result, job_completion







