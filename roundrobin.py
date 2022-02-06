def roundrobin(jobList, quantum=1):
   totalTime = 0
   currentList = []
   i = 0
   done = False
   finishedList = []
   while done != True:
      for job in jobList:
         if totalTime < job.arrival <= quantum + totalTime:
            currentList.append(job)
      if len(currentList) == 0:
         totalTime += 1
         continue
      currentJob = currentList[0]
      for job in currentList:
         if job != currentJob:
            if currentJob.remaining < quantum:
               job.wait += currentJob.remaining
               job.turnAround += currentJob.remaining
            else:
               job.wait += quantum
               job.turnAround += quantum
      if currentJob.remaining < quantum:
         currentJob.turnAround += currentJob.remaining
         currentJob.remaining -= currentJob.remaining
         #totalTime += currentJob.remaining
      else:
         currentJob.turnAround += quantum
         currentJob.remaining -= quantum
         #totalTime += quantum
      if currentJob.remaining == 0:
         finishedList.append(currentJob)
         currentList.remove(currentJob)
         print("Job %d -- Turnaround %3.2f Wait %3.2f" % (currentJob.num, currentJob.turnAround, currentJob.wait))
      else:
         currentList.remove(currentJob)
         currentList.append(currentJob)
         for job in currentList:
            if totalTime < job.arrival <= totalTime + quantum:
               currentList.remove(job)
               currentList.append(job)
      if currentJob.remaining < quantum:
         totalTime += currentJob.remaining
      else:
         totalTime += quantum
      if len(finishedList) == len(jobList):
         done = True
      for job in currentList:
         print(job)
         print(job.remaining)
         print(job.wait)
         print(job.turnAround)
         
   averageTurnAround = sum(map(lambda Job : Job.turnAround, jobList)) / len(jobList)
   averageWait = sum(map(lambda Job : Job.wait, jobList)) / len(jobList)
   print("Average -- Turnaround %3.2f Wait %3.2f" % (averageTurnAround, averageWait))
   return
