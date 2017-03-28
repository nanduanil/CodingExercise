# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 14:57:18 2017
https://www.hackerrank.com/challenges/unbounded-knapsack
@author: Nandu Anil
"""

def KnapSackCount(pendingAmount,changePosition):
    
    global coinList
    global coinVariations
    global targetAmount
    global maxValue
    
    #initialize dictionary for this pending amount
    if(pendingAmount not in dictCoinCombinations):
        dictCoinCombinations[pendingAmount] = [False] * coinVariations
    
    #check if this combination of amount and coin position,
    #has already been calculated
    if(dictCoinCombinations[pendingAmount][changePosition] == True):
        return
    
    currentCoin = coinList[changePosition]
    limit = pendingAmount//currentCoin
    
    currentMax = targetAmount - (pendingAmount - (limit * currentCoin))
    maxValue = max(maxValue,currentMax)
    
    #store the variation count into dictionary
    dictCoinCombinations[pendingAmount][changePosition] = True
     
    if(maxValue == targetAmount): return
    
    if((changePosition+1) <= (coinVariations-1)):
        for i in range(0,limit+1):
            newPendingAmount = pendingAmount - (currentCoin * i)        
            KnapSackCount(newPendingAmount,(changePosition+1))
            if(maxValue == targetAmount): return
    return 

            
import sys
sys.setrecursionlimit(10000)
testCases = int(sys.stdin.readline())

for j in range(0,testCases):
    coinVariations,targetAmount = [int(y) for y in sys.stdin.readline().split()]
    coinList = [int(y) for y in sys.stdin.readline().split()]
    maxValue = 0
    dictCoinCombinations = {} 
    if(coinVariations > 0 and targetAmount > 0):
        KnapSackCount(targetAmount,0)
    print(maxValue)

#==============================================================================
# import sys
# sys.setrecursionlimit(2050)
# 
# inArray = [line.rstrip('\n') for line in open('input02.txt')]
# testCases = int(inArray[0].strip())
# line = 1
# for j in range(0,testCases):
#     coinVariations,targetAmount = [int(x) for x in inArray[line].strip().split()]
#     line = line + 1
#     coinList = [int(x) for x in inArray[line].strip().split()]
#     line = line + 1
#     dictCoinCombinations = {}    
#     if(coinVariations > 0 and targetAmount > 0):
#         KnapSackCount(targetAmount,0)
#     print(maxValue)
#==============================================================================
