# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 15:20:15 2018


"""

import sys
from heapq import heappush, heappop

def checkAll(n, height, position):
    # Complete this function
    out = 'NONE'
    if(n < 1): return 'NONE'
    if(n == 1): return 'BOTH'
    stop = False
    fallRange = []
    heappush(fallRange,(height[0]+position[0])*-1)
    
    for i in range(1,n):
        if(position[i] <= -1*fallRange[0]):
            heappush(fallRange,(position[i] + height[i])*-1)
        else:
            stop = True
            break
    if not (stop): out = 'LEFT'
    stop = False
    fallRange = []
    heappush(fallRange,(position[-1]-height[-1]))
    for j in range(n-2,-1,-1):
        if(position[j] >= fallRange[0]):
            heappush(fallRange,(position[j]-height[j]))
        else:
            stop = True
            break
    if not (stop): 
        if(out == 'LEFT'): out = 'BOTH'
        else: out = 'RIGHT'
    return out
            

if __name__ == "__main__":
    n = int(input().strip())
    position = list(map(int, input().strip().split(' ')))
    height = list(map(int, input().strip().split(' ')))
    ret = checkAll(n, height, position)
    print(ret)
