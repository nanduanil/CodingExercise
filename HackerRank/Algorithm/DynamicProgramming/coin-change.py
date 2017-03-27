# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 14:04:47 2017
https://www.hackerrank.com/challenges/coin-change
@author: Nandu Anil
"""

def CoinCount(pendingAmount,changePosition):
    
    global coinList
    global coinVariations
    currentCoint = coinList[changePosition]
    limit = pendingAmount//currentCoint
    variation = 0
    
    #initialize dictionary for this pending amount
    if(pendingAmount not in dictCoinCombinations):
        dictCoinCombinations[pendingAmount] = [-1] * coinVariations
    
    #check if this combination of amount and coin position,
    #has already been calculated
    if(dictCoinCombinations[pendingAmount][changePosition] > -1):
        return dictCoinCombinations[pendingAmount][changePosition]

    for i in range(0,limit+1):
        newPendingAmount = pendingAmount - (currentCoint * i)
        if(newPendingAmount == 0):
            variation += 1
        elif((changePosition+1) <= (coinVariations-1)):
            variation = variation + CoinCount(newPendingAmount,(changePosition+1))
    #store the variation count into dictionary
    dictCoinCombinations[pendingAmount][changePosition] = variation
    return variation

            
import sys
totalAmount,coinVariations = [int(y) for y in sys.stdin.readline().split()]
coinList = [int(y) for y in sys.stdin.readline().split()]

#this dictionary will store variations possible in already calculated combination
# key of dictionary = amount left
# each key has a list with length of coinVariation

# Once we calculate variations for a combination of amount and coin position
# we store it into this dictionary
# We might come across the same problem again.
# The second time we encounter this problem we just fetch from this dictionary 
dictCoinCombinations = {}

variations = 0
if(coinVariations > 0 and totalAmount > 0):
    variations = CoinCount(totalAmount,0)
print(variations)