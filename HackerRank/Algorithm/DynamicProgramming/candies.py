# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 10:00:29 2017
https://www.hackerrank.com/challenges/candies
@author: Nandu
"""





import sys
numberOfChildren = int(input())
childrenRating = []
for i in range(0,numberOfChildren):
    childrenRating.append(int(input()))

decCount = 0
childrenCandies = [0] * numberOfChildren
if childrenRating[1] < childrenRating[0] :
    decCount = 1
elif childrenRating[1] > childrenRating[0]:
    childrenCandies[0] = 1
    childrenCandies[1] = 2
elif childrenRating[1] == childrenRating[0]:
    childrenCandies[0] = 1
    childrenCandies[1] = 1

for i in range(2,numberOfChildren):
    if childrenRating[i] < childrenRating[i-1] :
        decCount += 1
    elif childrenRating[i] > childrenRating[i-1]:
        if(decCount > 0):
            k = i-2
            childrenCandies[i-1] = 1 
            for _ in range(decCount-1):
                if(childrenRating[k] == childrenRating[k+1]):
                    childrenCandies[k] = 1
                else:
                    childrenCandies[k] = childrenCandies[k+1] + 1
                k -= 1
            if(childrenCandies[k] < childrenCandies[k+1]):
                childrenCandies[k] = childrenCandies[k+1] + 1                
            decCount = 0
        else:
            childrenCandies[i] = childrenCandies[i-1] + 1
    elif childrenRating[i] == childrenRating[i-1]:
        if(decCount>0):
            decCount += 1
        else:
            childrenCandies[i] = 1

print(sum(childrenCandies))
