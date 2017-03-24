# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 13:56:24 2017
https://www.hackerrank.com/challenges/dijkstrashortreach
@author: nanil
"""
#==============================================================================
# #This section is to read input from file
# from heapq import heappush, heappop
# import itertools
# import time
# #inArray = [line.rstrip('\n') for line in open('dijk_in07.txt')]
# inArray = [line.rstrip('\n') for line in open('dijk_in01.txt')]
# testCases = int(inArray[0])
# line = 1
# startTime = time.time()
# for t in range(0,testCases):
#     counter = itertools.count()
#     command = [int(x) for x in inArray[line].strip().split()]
#     line = line + 1
#     numberOfNodes = command[0]
#     graph = [dict() for i in range(0, numberOfNodes+1)]
#     for c in range(0,command[1]):
#         (fromNode,toNode,weight) = [int(y) for y in inArray[line].strip().split()]
#         line = line + 1
#         weight = weight if toNode not in graph[fromNode] else min(weight, graph[toNode][fromNode])
#         graph[fromNode][toNode] = weight
#         graph[toNode][fromNode] = weight
#     startNode = int(inArray[line])
#     line = line + 1  
#     print(time.time()-startTime)
#==============================================================================
from heapq import heappush, heappop
import itertools
import sys
testCases = int(input())

for t in range(0,testCases):
    counter = itertools.count()
    command = [int(x) for x in input().strip().split()]
    numberOfNodes = command[0]
    graph = [dict() for i in range(0, numberOfNodes+1)]

    for c in range(0,command[1]):
        (fromNode,toNode,weight) = [int(y) for y in sys.stdin.readline().split(' ')]
        #store only the minimum edge between two nodes
        weight = weight if toNode not in graph[fromNode] else min(weight, graph[toNode][fromNode])
        graph[fromNode][toNode] = weight
        graph[toNode][fromNode] = weight
    startNode = int(input())
    
    crossHeap = []
    explored = [-1] * (numberOfNodes+1) #this will contain distance of nodes
    heappush(crossHeap, [0,next(counter),startNode])
    
    #run until there are edges from explored to unexplored
    while(len(crossHeap) > 0):

        (smallestDistance,counterData,nextNode) = heappop(crossHeap)
        #if the minimum one selected has already been explored, continue
        if(explored[nextNode] > -1):
            continue
        
        explored[nextNode] = smallestDistance
        
        #update the adjacent nodes to the ones explored, which are yet to be explored
        for toNode in graph[nextNode]:
            if(explored[toNode] == -1):
                distance = explored[nextNode] + graph[nextNode][toNode]
                newEntry = [distance,next(counter),toNode]
                heappush(crossHeap,newEntry)
            
    for i in range(1,numberOfNodes+1):
        if(i != startNode):
            print(explored[i],end=" ")
    print("")
            
#print(time.time()-startTime)

                