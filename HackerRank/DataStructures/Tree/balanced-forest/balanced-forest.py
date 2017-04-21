# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 12:03:04 2017
https://www.hackerrank.com/challenges/balanced-forest
"""

#%%
import math
import copy
import sys
sys.setrecursionlimit(60000)


#this will navigate the graph and calculate the values when each edge is broken
#it stores the values and the edge details in dictionary
def DFS_Recursive(graph,currentNode,splitGraph,totalCoins,explored_global):
    explored_global[currentNode] = True
    if(currentNode not in graph):
        return
    totSplitValue = coins[currentNode-1]
    for node in graph[currentNode]:
        if(node not in explored_global):
            splitValue = DFS_Recursive(graph,node,splitGraph,totalCoins,explored_global)
            if(splitValue in splitGraph):
                splitGraph[splitValue].append([node,currentNode])
                splitGraph[totalCoins-splitValue].append([currentNode,node])
            else:
                splitGraph[splitValue] = [[node,currentNode]]
                splitGraph[totalCoins-splitValue] = [[currentNode,node]]
            totSplitValue = totSplitValue + splitValue
    return totSplitValue

#will find a leaf to start checking split values
def FindLeaf(graph,node):
    explored = {}
    toContinue = True
    while(toContinue):
        toContinue = False
        for n in graph[node]:
            if(n in explored):
                continue
            else:
                node = n
                explored[n] = True
                toContinue = True
                break
        
    return node
    
def FindOutput(graph,coins):
    totalCoins = sum(coins)
    idealSplit = math.ceil(totalCoins/3)
    outOfBoundSplit = math.ceil(totalCoins/2)
    
    leafNode = FindLeaf(graph,1)
    splitGraphFirst = {}
    explored_global = {}
    
    #find the split values
    DFS_Recursive(graph,leafNode,splitGraphFirst,totalCoins,explored_global)
    splitGraphFirst[totalCoins] = True
    explored_global = {}
    smallestChosenSplit = totalCoins+1
    
    #loop through all the values
    for currentSplit in splitGraphFirst:
        #split value should be >= totalValue/3 if we have to create 3 trees
        #split should be less than totalValue/2, else we cannot create 3 trees
        if(currentSplit >= idealSplit and currentSplit <= outOfBoundSplit):
            #if split found is already lesser
            if(currentSplit>smallestChosenSplit):
                continue
            
            #split is possible if there are 2 edge breakage which have the current split
            if(len(splitGraphFirst[currentSplit]) > 1):
                if(currentSplit < smallestChosenSplit):
                    smallestChosenSplit = currentSplit
                    
            #if double the split value not present then no chance of creating 3 trees
            if 2*currentSplit not in splitGraphFirst:
                continue
            
            pendingGraph = copy.deepcopy(graph)
            fromEdge,toEdge = splitGraphFirst[currentSplit][0]
            
            #break the selected edge
            pendingGraph[fromEdge].remove(toEdge)
            pendingGraph[toEdge].remove(fromEdge)
            
            leafNode = FindLeaf(pendingGraph,toEdge)
            splitGraphSecond = {}
            explored_global = {}
            newTotalCoins = totalCoins - currentSplit
            splitGraphSecond[newTotalCoins] = True
            
            #find new split values after breaking
            DFS_Recursive(pendingGraph,leafNode,splitGraphSecond,newTotalCoins,explored_global)
            explored_global = {}
            if(currentSplit in splitGraphSecond):
                if(currentSplit < smallestChosenSplit):
                    smallestChosenSplit = currentSplit
    if(smallestChosenSplit == totalCoins+1):
        return -1
    else:
        return smallestChosenSplit
    


numberOfTrees = int(input())

for t in range(numberOfTrees):
    numberOfNodes = int(input())
    coins = [int(c) for c in input().strip().split()]
    graph = {}
    for n in range(numberOfNodes-1):
        firstNode,secondNode = [int(n) for n in input().strip().split()]
        if(firstNode in graph):
            graph[firstNode].append(secondNode)
        else:
            graph[firstNode] = [secondNode]
        
        if(secondNode in graph):
            graph[secondNode].append(firstNode)
        else:
            graph[secondNode] = [firstNode]
    
    chosenSplit = 0
    if(len(graph) > 0):
        chosenSplit = FindOutput(graph,coins)
    extraCoin = -1
    if(chosenSplit > 0):
        extraCoin = 3*chosenSplit - sum(coins)
        
    print(extraCoin)
    
    
#==============================================================================
# #read from file    
# import time    
# inArray = [line.rstrip('\n') for line in open('C:\\Users\\nanil\\Desktop\\CodingExercise\\HackerRank\\DataStructures\\Tree\\balanced-forest\\input4.txt')]
# 
# numberOfTrees = int(inArray[0].strip())
# line = 1
# initStartTime = time.time()
# for t in range(numberOfTrees):
#     numberOfNodes = int(inArray[line].strip())
#     line += 1
#     coins = [int(c) for c in inArray[line].strip().split()]
#     line += 1
#     graph = {}
#     for n in range(numberOfNodes-1):
#         firstNode,secondNode = [int(n) for n in inArray[line].strip().split()]
#         line += 1                        
#         if(firstNode in graph):
#             graph[firstNode].append(secondNode)
#         else:
#             graph[firstNode] = [secondNode]
#         
#         if(secondNode in graph):
#             graph[secondNode].append(firstNode)
#         else:
#             graph[secondNode] = [firstNode]
#     
#     runTime = time.time() - initStartTime
#     print("read:", runTime)
#     print(" ")
# 
#     startTime = time.time()
#     chosenSplit = 0
#     if(len(graph) > 0):
#         chosenSplit = FindOutput(graph,coins)
#         runTime = time.time() - startTime
#         print("run:", runTime)
#     extraCoin = -1
#     if(chosenSplit > 0):
#         extraCoin = 3*chosenSplit - sum(coins)
#         
#     print(extraCoin)
# 
# print("total run:", time.time()-initStartTime)
#==============================================================================
