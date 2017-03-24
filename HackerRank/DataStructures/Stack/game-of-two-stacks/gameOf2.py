# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 09:55:21 2017
https://www.hackerrank.com/challenges/game-of-two-stacks
@author: Nandu Anil
"""
#!/bin/python3

import collections

inArray = [line.rstrip('\n') for line in open('C:\\Users\\nanil\\Desktop\\Algo\\HackerRank\\Stack\\gameOf2_in7.txt')]
#outArray = [line.rstrip('\n') for line in open('heap_input04.txt')]
g = int(inArray[0])
#print(inArray)
for a0 in range(g):
    value = a0 * 3
    n,m,x = inArray[value+1].strip().split(' ')
    n,m,x = [int(n),int(m),int(x)]
    a = collections.deque(map(int, inArray[value+2].strip().split(' ')))
    b = collections.deque(map(int, inArray[value+3].strip().split(' ')))
    #print(a)
    #print(b)
#==============================================================================
# g = int(input().strip())
# for a0 in range(g):
#     n,m,x = input().strip().split(' ')
#     n,m,x = [int(n),int(m),int(x)]
#     a = collections.deque(map(int, input().strip().split(' ')))
#     b = collections.deque(map(int, input().strip().split(' ')))
#==============================================================================

    count = 0
    sum = 0
    while(len(a)>0 or len(b)>0):
        chooseA = False
        chooseB = False
        checkA = False
        checkB = False
        if(len(a)>0):
            checkA = True
        if(len(b)>0):
            checkB = True
        if(checkA  and checkB):
            if(a[0] <= b[0]):
                chooseA = True
            else:
                chooseB = True
        elif(checkA):
            chooseA = True
        elif(checkB):
            chooseB = True
        
        if(chooseA):
            tempSum = sum + a.popleft()
        elif(chooseB):
            tempSum = sum + b.popleft()
        if(tempSum <= x):
            sum = tempSum
            count += 1
        else:
            print(count)
            break