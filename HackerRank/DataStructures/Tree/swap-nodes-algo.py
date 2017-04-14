# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 10:13:31 2017
https://www.hackerrank.com/challenges/swap-nodes-algo
"""
#%%

import collections
import sys 
sys.setrecursionlimit(15000)

#This will traverse the graph and return a dictionary
#key of dictionary = level
#value = nodes in that level
def BFS(graph,startNode):
    explored = {}
    levelTrack = {}    
    workerQueue = collections.deque()
    workerQueue.append(startNode)
    explored[startNode] = 1
    levelTrack[1] = [startNode]
    while(len(workerQueue) > 0):
        currentNode = workerQueue.popleft()
        nextLevel = explored[currentNode] + 1
        for node in graph[currentNode]:
            if(node < 1): continue
            if(node not in explored): 
                explored[node] = nextLevel
                if(nextLevel in levelTrack):
                    levelTrack[nextLevel].append(node)
                else:
                    levelTrack[nextLevel] = [node]
                workerQueue.append(node)         
    return levelTrack 

#%%
#in order traversal of graph
def traverseGraph(graph,node):
    leftNode,rightNode = graph[node]
    if(leftNode > 0):
        traverseGraph(graph,leftNode)
    print(node,end=" ")
    if(rightNode > 0):
        traverseGraph(graph,rightNode)
    
#%%
numberOfnodes = int(input())

graph = {}
for i in range(1,numberOfnodes+1):
    graph[i] = [int(j) for j in input().strip().split()]
    
#calulate the nodes in each level
graphLevel = BFS(graph,1)
numberOfLevel = len(graphLevel)

numberOfSwaps = int(input())
for k in range(numberOfSwaps):
    swapStart = int(input())
    
    #loop through all the levels to swap
    for swapLevel in range(swapStart,numberOfLevel,swapStart):
        
        #loop through all the nodes in the level
        for swapNode in graphLevel[swapLevel]:
            
            #reverse the nodes at a node
            graph[swapNode] = list(reversed(graph[swapNode]))
    
    traverseGraph(graph,1)
    print()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
