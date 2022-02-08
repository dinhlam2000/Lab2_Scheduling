import sys
from fifo import *
from shortestRemaining import *
from roundrobin import *

class Job:
   turnAround = 0
   wait = 0
   num = 0
   # response = 0
   remaining = 0
   finish = 0
   def __init__(self, arrival, runtime):
      self.arrival = arrival
      self.runtime = runtime
      self.remaining = runtime
   def __repr__(self):
      rep = f'Job(arrival = {self.arrival}, runtime = {self.runtime})'
      return rep

def main():
   jobList = []
   if len(sys.argv) < 2:
      print("Insufficient arguments")
      return
   with open(sys.argv[1]) as f:
      line = f.readline()
      while line:
         line = line.split()
         jobList.append(Job(int(line[1]), int(line[0])))
         line = f.readline()
   jobList.sort(key=lambda Job: Job.arrival)
   i = 0
   for job in jobList:
      job.num = i
      i += 1
   fifo(jobList)
   #roundrobin(jobList, 1)
   #shortestRemaining(jobList)
   



















if __name__ == "__main__":
    main()
