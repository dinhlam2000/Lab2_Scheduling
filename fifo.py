def fifo(jobList):
   # jobList.sort(key=lambda Job: Job.arrival)
   # i = 0
   totalTime = 0
   for job in jobList:
      # job.num = i
      # i += 1
      if totalTime == 0:
         job.wait = 0
         # job.response = job.wait + 1
         totalTime += job.runtime
         job.turnAround = totalTime
         job.finish = totalTime
      else:
         job.wait = totalTime - job.arrival
         # job.response = totalTime - job.arrival + 1
         job.turnAround = totalTime - job.arrival + job.runtime
         totalTime += job.runtime
         job.finish = totalTime
      print("Job %3d -- Turnaround %3.2f Wait %3.2f" % (job.num, job.turnAround, job.wait))
   
   averageTurnAround = sum(map(lambda Job : Job.turnAround, jobList)) / len(jobList)
   averageWait = sum(map(lambda Job : Job.wait, jobList)) / len(jobList)
   print("Average -- Turnaround %3.2f Wait %3.2f" % (averageTurnAround, averageWait))
   return
