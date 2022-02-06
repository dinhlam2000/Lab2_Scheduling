#How to start
```bash
- pip3 install -r requirements.txt
- virtualenv venv
- source venv/bin/activate

```


#To run schedSim.py
```bash
python3 schedSim.py <file> -p <algorithm> <optional args>

<file> --> path to jobs.txt file
-p --> indicates the algorithm, FIFO, RR, SRTN
-q --> Quantum used for round robin, not required, but default would just be 1

OUTPUT: Console output --> All jobs including its wait time and turn around time
                       --> Average wait time and turn around time

```