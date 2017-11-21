# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 14:04:27 2017
https://www.hackerrank.com/challenges/maximize-it

"""

import itertools

numOflines,moduloValue =  list(map(int, input().strip().split()))
lines = []                           

for y in range(numOflines):
    lines.append(list(map(int, input().strip().split()))[1:])

maxModulo = 0

for combo in itertools.product(*lines):
    maxModulo = max(sum(list(map(lambda x: (x*x), combo)))%moduloValue,maxModulo)
    
print(maxModulo)


