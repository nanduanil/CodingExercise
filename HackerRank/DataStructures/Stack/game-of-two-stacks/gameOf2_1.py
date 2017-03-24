# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 11:53:08 2017

@author: nanil
"""

g = int(input().strip())
for a0 in range(g):
    n,m,x = input().strip().split(' ')
    n,m,x = [int(n),int(m),int(x)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    countA = 0
    countB = 0
    count = 0
    tot = 0 
    for i in range(0,len(a)):
        tot = tot + a[i]
        if(tot > x):
            break
        countA += 1
    tot = 0
    for i in range(0,len(b)):
        tot = tot + b[i]
        if(tot > x):
            break
        countB += 1
    if(countA>countB):
        count = countA
    else:
        count = countB
    
    for i in range(0,countA+1):
        tot = 0
        tempCount = 0
        for j in range(0,i):
            tempCount = tempCount + 1
            tot = tot + a[j]  
        k = 0
        while(k < len(b)):
            tempSum = tot + b[k]
            if(tempSum > x):
                break
            else:
                tot = tempSum
                tempCount = tempCount  +1
                k = k + 1
        if(tempCount > count):
            count = tempCount
    print(count)                