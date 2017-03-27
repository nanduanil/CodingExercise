# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 10:42:48 2017
https://www.hackerrank.com/challenges/insertion-sort
@author: Nandu Anil
"""

#this is implementing mergesort
def recurseFindInversion(intList,n):
    global countOfInverse
    splitLenList = n//2
    #create left and right array
    intList1 = intList[0:splitLenList]
    intList2 = intList[splitLenList:]

    leftLength = splitLenList
    rightLength = (n-splitLenList)
    #call recursion if left or right array have more than one element
    if(leftLength > 1):
        intList1 = recurseFindInversion(intList1,leftLength)  
    if(rightLength > 1):
        intList2 = recurseFindInversion(intList2,rightLength)
    intListSorted = []
    i = 0
    j = 0
    #merge the sorted sub arrays
    while (leftLength > 0 and rightLength > 0):
        if(intList1[i] <= intList2[j]):
            intListSorted.append(intList1[i])
            i = i + 1
            leftLength = leftLength - 1
        elif(intList1[i] > intList2[j]):
            intListSorted.append(intList2[j])
            countOfInverse = countOfInverse + leftLength
            j = j + 1
            rightLength = rightLength - 1
    if(leftLength > 0):
        intListSorted.extend(intList1[i:])
    if(rightLength > 0):
        intListSorted.extend(intList2[j:])
    
    return intListSorted
    
    
import sys
numberOfTestCase = int(sys.stdin.readline())
for i in range(0,numberOfTestCase):
    arrayLength = int(sys.stdin.readline())
    intList = [int(y) for y in sys.stdin.readline().split()]
    countOfInverse = 0    
    sortedArray = recurseFindInversion(intList,arrayLength)
    print(countOfInverse)




