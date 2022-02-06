import sys
import copy

from roundrobin import roundrobin
from collections import defaultdict
from fifo import fifo
def parser_helper(lines):
    interrupts = defaultdict(list)
    jobs_amount = {}
    jobs_arrival = {}


    job_counter = 0

    lines = list(map(lambda x: x.split(), lines))
    lines = sorted(lines, key=lambda x: x[1]) #sort jobs based on arrival time
    # import pdb; pdb.set_trace()
    for line in lines:
        amount = int(line[0])
        arrival = int(line[1])
        # import pdb; pdb.set_trace()
        interrupts[arrival].append(job_counter)
        jobs_amount[job_counter] = amount
        jobs_arrival[job_counter] = arrival
        job_counter += 1


    return interrupts, jobs_amount, jobs_arrival


# Turn Around Time: total time the process exists in the system. (completion time – arrival time).
# Waiting Time: total time waiting for their complete execution. (turn around time – burst time ).
def turn_around_time(jobs_arrival,job_completion):
    turn_around_time = {}
    for job, arrival in jobs_arrival.items():
        turn_around_time[job] = job_completion[job] - arrival
        pass
    return turn_around_time

def waiting_time(job_burst_time, job_turn_around_time):
    waiting_time = {}
    for job, burst_time in job_burst_time.items():
        waiting_time[job] = job_turn_around_time[job] - burst_time
    return waiting_time


if __name__ == "__main__":
    file_name = sys.argv[1]

    with open('jobs.txt', 'r') as file:
        lines = file.readlines()


    interrupts, jobs, jobs_arrival = parser_helper(lines)
    import pdb; pdb.set_trace()
    result, job_completion = roundrobin(copy.deepcopy(interrupts),copy.deepcopy(jobs),2)
    result2, job_completion2 = fifo(copy.deepcopy(interrupts), copy.deepcopy(jobs))

    turn_around_time = turn_around_time(jobs_arrival, job_completion)
    waiting_time = waiting_time(jobs, turn_around_time)

    for job in jobs:
        print("Job {0}: ----- Turn Around Time = {1}    Waiting Time = {2}".format(job,turn_around_time[job], waiting_time[job]))
    import pdb; pdb.set_trace()

