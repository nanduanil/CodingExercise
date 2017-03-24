# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 15:07:48 2017
https://www.hackerrank.com/challenges/minimum-average-waiting-time
@author: nanil
"""

from heapq import heappush, heappop
allOrderHeap = []
queryCountString = input()
queryCount = int(queryCountString)
customerWaitHeap = []
totalCustomers = queryCount    
totalWaitingTime = 0
currentTime = 0

#get all the inputs and store them in a heap with the input time as the ordering
#so we can extract the orders in increasing order of entryTime    
for q in range(0,queryCount):
    command =[int(x) for x in input().split()]
    entryTime = command[0]
    entryCount = q
    runTime = command[1]
    heappush(allOrderHeap,[entryTime,entryCount,runTime])

def UpdateWaitHeap(currentTime):
    #if next order can be considered to be in working queue
    while(allOrderHeap[0][0] < currentTime):
        entryTime,entryCount,runTime = heappop(allOrderHeap)
        heappush(customerWaitHeap,[runTime,entryCount,entryTime])
        #if all orders moved to working queue
        if(len(allOrderHeap)==0):
            break
    #if working queue is null, this means gap in customer entry
    #move current time to the next orders entry time
    if(len(customerWaitHeap) == 0):
        entryTime,entryCount,runTime = heappop(allOrderHeap)
        heappush(customerWaitHeap,[runTime,entryCount,entryTime])
        currentTime = entryTime
    return currentTime
    
#keep working until all the orders are processed
while(len(allOrderHeap)>0 or len(customerWaitHeap)>0):
    #if pending orders in input queue then update working queue
    if(len(allOrderHeap)>0):
        currentTime = UpdateWaitHeap(currentTime)
    #pop the next one from the working queue
    #out of all the ones from the working queue take the one with least runtime
    #this ensures smallest average wait time
    runTime,entryCount,entryTime = heappop(customerWaitHeap)    
    totalWaitingTime = totalWaitingTime + ((currentTime-entryTime) + runTime)
    currentTime = currentTime + runTime
        
print(int(totalWaitingTime/totalCustomers))
