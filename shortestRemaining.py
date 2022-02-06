def shortestRemaining(jobList):
   currentList = []
   finishedList = []
   done = False
   totalTime = 0
   while done != True:
      for job in jobList:
         if job.arrival == totalTime:
            currentList.append(job)
      if len(currentList) == 0:
         totalTime += 1
         continue
      minRemaining = currentList[0]
      for job in currentList:
         if job.remaining < minRemaining.remaining:
            minRemaining = job
      for job in currentList:
         if job != minRemaining:
            job.wait += 1
            job.turnAround += 1
      minRemaining.turnAround += 1
      minRemaining.remaining -= 1
      if minRemaining.remaining == 0:
         finishedList.append(minRemaining)
         currentList.remove(minRemaining)
         print("Job %3d -- Turnaround %3.2f Wait %3.2f" % (minRemaining.num, minRemaining.turnAround, minRemaining.wait))
      if len(finishedList) == len(jobList):
         done = True
      totalTime += 1
   averageTurnAround = sum(map(lambda Job : Job.turnAround, jobList)) / len(jobList)
   averageWait = sum(map(lambda Job : Job.wait, jobList)) / len(jobList)
   print("Average -- Turnaround %3.2f Wait %3.2f" % (averageTurnAround, averageWait))
   return
