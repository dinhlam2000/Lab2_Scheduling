def fifo(jobList):
   totalTime = 0
   for job in jobList:
      if totalTime == 0:
         job.wait = 0
         totalTime += job.runtime
         job.turnAround = totalTime
         job.finish = totalTime
      else:
         job.wait = totalTime - job.arrival
         job.turnAround = totalTime - job.arrival + job.runtime
         totalTime += job.runtime
         job.finish = totalTime
      print("Job %3d -- Turnaround %3.2f Wait %3.2f" % (job.num, job.turnAround, job.wait))
   
   averageTurnAround = sum(map(lambda Job : Job.turnAround, jobList)) / len(jobList)
   averageWait = sum(map(lambda Job : Job.wait, jobList)) / len(jobList)
   print("Average -- Turnaround %3.2f Wait %3.2f" % (averageTurnAround, averageWait))
   return
