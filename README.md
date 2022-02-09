#How to start
```bash
- pip3 install -r requirements.txt
- virtualenv venv
- source venv/bin/activate

```


#To run schedSim.py
```bash
python3 schedSim.py <file> -p <algorithm> <optional args>

or 

./schedSim <file> -p <algorithm> <optional args>

<file> --> path to jobs.txt file
-p --> indicates the algorithm, FIFO, RR, SRTN
-q --> Quantum used for round robin, not required, but default would just be 1

OUTPUT: Console output --> All jobs including its wait time and turn around time
                       --> Average wait time and turn around time

```

#Questions
```bash
1. For what types of workloads does SRTN deliver the same turnaround times as FIFO?

STRN delivers the same turnaround times as FIFO when the input jobs are already in order of smallest jobs first.
This can also happen if all of the burst times of the jobs are the same length. Finally, if the jobs are increasing
in size, for example the second is bigger than the first and the third is bigger than the second.

2. For what types of workloads and quantum lengths does SRTN deliver the same response times as RR?

SRTN and RR have similar response times when the burst times are low and the quantum lengths are as long or longer
than the longest burst time.

3. What happens to response time with SRTN as job lengths increase? Can you use the simulator to demonstrate the trend?

Response time with SRTN becomes much longer as job lengths increase. An example is seen below:

Input Jobs:
50 27
108 38
700 43
220 54
901 80

Output with Response Time:

Job   0 -- Response 1.00 Turnaround 50.00 Wait 0.00
Job   1 -- Response 40.00 Turnaround 147.00 Wait 39.00
Job   3 -- Response 132.00 Turnaround 351.00 Wait 131.00
Job   2 -- Response 363.00 Turnaround 1062.00 Wait 362.00
Job   4 -- Response 1026.00 Turnaround 1926.00 Wait 1025.00
Average -- Response 312.40 Turnaround 707.20 Wait 311.40\

What happens to response time with RR as quantum lengths increase? Can you write an equation that gives the worst-case response time, given N jobs?

Response time grows as the quantum increases in length. An equation for this is seen below:

Worst case response time for N jobs = quantum * (N-1)

```
