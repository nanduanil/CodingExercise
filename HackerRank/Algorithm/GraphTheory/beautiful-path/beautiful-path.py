# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 09:02:56 2017
https://www.hackerrank.com/challenges/beautiful-path
@author: nandu
"""
#==============================================================================
# #%%
# from heapq import heappop,heappush
# inArray = [line.rstrip('\n') for line in open('in.txt')]
# numberOfnode , numberOfedges = [int(x) for x in inArray[0].strip().split()]
# line = 1
# graph = [dict() for i in range(0, numberOfnode+1)]
# #graph = {}
# for i in range(0,numberOfedges):
#     fromNode,toNode,penalty = [int(x) for x in inArray[line].strip().split()]
#     line += 1
#     if(fromNode==toNode) : continue
#     if(toNode not in graph[fromNode]):
#         graph[fromNode][toNode] = {}
#         graph[toNode][fromNode] = {}
#     graph[fromNode][toNode][penalty] = 0
#     graph[toNode][fromNode][penalty] = 0
#          
# startNode,endNode = [int(x) for x in inArray[-1].strip().split()]
# 
#==============================================================================
#%%
from heapq import heappop,heappush
numberOfnode , numberOfedges = [int(y) for y in input().split()]
graph = [dict() for i in range(0, numberOfnode+1)]
#graph = {}
for i in range(0,numberOfedges):
    fromNode,toNode,penalty = [int(y) for y in input().split()]
    if(fromNode==toNode) : continue
    if(toNode in graph[fromNode]):
        penalty = min(penalty,graph[fromNode][toNode])
    graph[fromNode][toNode] = penalty
    graph[toNode][fromNode] = penalty
         
startNode,endNode = [int(y) for y in input().split()]

#logic using dijkstra's ; but this does not work for the conditions in this question
crossHeap = []
distances = [-1] * (numberOfnode+1)
heappush(crossHeap,[0,startNode])
while(len(crossHeap)>0):
    distance,nextNode = heappop(crossHeap)
    #node already explored
    if(distances[nextNode] > -1):
        continue
    
    #store selected node's distance
    distances[nextNode] = distance
    
    #end Node reached
    if(nextNode == endNode):break

    #update the adjacent node's that are not explored
    for toNode in graph[nextNode]:
        #node already explored
        if(distances[toNode] > -1):continue
        
        newDistance = graph[nextNode][toNode] | distance
        heappush(crossHeap,[newDistance,toNode])
        
print(distances[endNode])


