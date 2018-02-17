# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 14:44:13 2018

https://www.hackerrank.com/contests/rookierank-4/challenges/exam-rush
"""
import sys

def examRush(tm, t):
    sortedTime = sorted(tm)
    result = 0
    totTime = 0
    i = 0
    for i in range (len(sortedTime)):
        totTime = totTime + sortedTime[i]
        if(totTime > t): 
            break
        else:
            result = result + 1
    return i
    
        
    

if __name__ == "__main__":
    n, t = input().strip().split(' ')
    n, t = [int(n), int(t)]
    tm = []
    tm_i = 0
    for tm_i in range(n):
       tm_t = int(input().strip())
       tm.append(tm_t)
    result = examRush(tm, t)
    print(result)