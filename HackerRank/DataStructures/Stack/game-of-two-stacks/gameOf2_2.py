# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 10:51:58 2017
https://www.hackerrank.com/challenges/game-of-two-stacks
@author: Nandu Anil
"""

#==============================================================================
# inArray = [line.rstrip('\n') for line in open('C:\\Users\\nanil\\Desktop\\Algo\\HackerRank\\Stack\\gameOf2_in7.txt')]
# #outArray = [line.rstrip('\n') for line in open('heap_input04.txt')]
# g = int(inArray[0])
# #print(inArray)
# for a0 in range(g):
#     value = a0 * 3
#     n,m,x = inArray[value+1].strip().split(' ')
#     n,m,x = [int(n),int(m),int(x)]
#     a = list(map(int, inArray[value+2].strip().split(' ')))
#     b = list(map(int, inArray[value+3].strip().split(' ')))
# 
#     #print(a)
#     #print(b)
#==============================================================================
g = int(input().strip())
for a0 in range(g):
    n,m,x = input().strip().split(' ')
    n,m,x = [int(n),int(m),int(x)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    countA = 0
    countB = 0
    count = 0
    countA_dict = {}
    countA_dict[0] = 0
    tot = 0
    #find count if only taking from stack A
    for i in range(0,len(a)):
        tot = tot + a[i]
        if(tot > x):
            break
        countA_dict[i+1] = tot
        countA += 1
    
    count = countA
    totB = 0
    countB = 0
    sumB = 0
    #this look looks for total count when taking items 0 to max possible from A
    #max possible from A is the countA found above
    for i in range(countA,-1,-1):
        totA = countA_dict[i]
        #as we reduce count from A we need only start from the last item
        #we could take from B
        k = countB
        while(k < len(b)):
            tempSumB = sumB + b[k]
            if(tempSumB + totA> x):
                break
            else:
                sumB = tempSumB
                countB = countB  +1
                k = k + 1
        tempCount = i + countB
        if(tempCount > count):
            count = tempCount
    print(count)                
            
            
            
            
            
            
            
            
            
            
            
            
            
    