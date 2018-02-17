# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 09:05:32 2018
height-and-total-height-of-a-bst
"""

import os
import sys

class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
# Complete the function below.

def insertBST(treeNode,value):
    if(treeNode.data > value):
        if(not(treeNode.left)):
            treeNode.left = node(value)
        else:
            insertBST(treeNode.left,value)
    elif(treeNode.data < value):
        if(not(treeNode.right)):
            treeNode.right = node(value)
        else:
            insertBST(treeNode.right,value)


def calculateHeight(treeNode,heightDict):
    if(treeNode.left):
        calculateHeight(treeNode.left,heightDict)
        if(heightDict[treeNode.left.data] + 1 > heightDict[treeNode.data]):
            heightDict[treeNode.data] = heightDict[treeNode.left.data] + 1
    if(treeNode.right):
        calculateHeight(treeNode.right,heightDict)
        if(heightDict[treeNode.right.data] + 1 > heightDict[treeNode.data]):
            heightDict[treeNode.data] = heightDict[treeNode.right.data] + 1
    


def heightAndTotalHeight(arr):
    # Write your code here.
    rootTree = node(arr[0])
    heightDict = {}
    heightDict[arr[0]] = 0
    for insertNum in arr[1:]:
        insertBST(rootTree,insertNum)
        heightDict[insertNum] = 0
    calculateHeight(rootTree,heightDict)
    
    sumOfHeights = 0
    for i in heightDict.items():
        sumOfHeights = sumOfHeights + i[1]
    
    return [heightDict[arr[0]],sumOfHeights]
        
    


if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    arr_size = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = heightAndTotalHeight(arr)

    print(map(str, result))














