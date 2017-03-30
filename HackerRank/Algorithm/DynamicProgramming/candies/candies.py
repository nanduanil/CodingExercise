# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 10:00:29 2017
https://www.hackerrank.com/challenges/candies
@author: Nandu
"""
#==============================================================================
# #read input from file
# inArray = [line.rstrip('\n') for line in open('input07.txt')]
# numberOfChildren = int(inArray[0].strip())
# line =1
# childrenRating = []
# for i in range(0,numberOfChildren):
#     childrenRating.append(int(inArray[line].strip()))
#     line += 1
#==============================================================================

numberOfChildren = int(input())
childrenRating = []
for i in range(0,numberOfChildren):
    childrenRating.append(int(input()))
    
decCount = 0
childrenCandies = [0] * numberOfChildren
                  
#initialize candy for first 2 children
if childrenRating[1] < childrenRating[0] :
    decCount = 1
elif childrenRating[1] > childrenRating[0]:
    childrenCandies[0] = 1
    childrenCandies[1] = 2
elif childrenRating[1] == childrenRating[0]:
    childrenCandies[0] = 1
    childrenCandies[1] = 1

#when a minimum is found we go from minimum to the peak before the minimum
#we update each children with one more candy than the previous one
def updateChildrenCandies(i):
    global childrenCandies
    global childrenRating
    global decCount
    k = i-2
    childrenCandies[i-1] = 1 
    for _ in range(decCount-1):
        if(childrenRating[k] == childrenRating[k+1]):
            childrenCandies[k] = 1
        else:
            childrenCandies[k] = childrenCandies[k+1] + 1
        k -= 1
    #check if peak already has a greater value.
    #else update the peak
    if(childrenCandies[k] <= childrenCandies[k+1]):
        childrenCandies[k] = childrenCandies[k+1] + 1                
    


for i in range(2,numberOfChildren):
    #if decreasing increment the decreasing count
    #after reaching minimum we update candies for them
    if childrenRating[i] < childrenRating[i-1] :
        decCount += 1
        #if already reached the end of the children list, we cannot wait for increase
        if(i == numberOfChildren - 1):
            updateChildrenCandies(i+1)
    #if increasing
    elif childrenRating[i] > childrenRating[i-1]:
        #if this increase is after decrease, we crossed a minimum.
        #update the candies for minumum to the peak on the other side.
        if(decCount > 0):
            updateChildrenCandies(i)
            decCount = 0
        #update the current candy more than the previous value
        childrenCandies[i] = childrenCandies[i-1] + 1
    #if the same value as previous
    elif childrenRating[i] == childrenRating[i-1]:
        #if same value in between decreasing slope
        if(decCount>0):
            decCount += 1
            if(i == numberOfChildren - 1):
                updateChildrenCandies(i+1)
        #if same value in between increasing slope
        else:
            childrenCandies[i] = 1

print(sum(childrenCandies))
