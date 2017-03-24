# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 15:34:33 2017
problem : https://www.hackerrank.com/challenges/qheap1
@author: nanil
"""

#%%
import collections
import math
class MyHeap():
    
    def __init__(self):
        self.heapData = collections.deque()
        self.outData = []
    
        
    def MinItem(self):
        self.outData.append(self.heapData[0])
        return self.heapData[0]
    
    def AddItem(self,item):
        self.heapData.append(item)
        childNode = len(self.heapData) - 1
        while(childNode > 0):
            parentNode = math.ceil(childNode/2) - 1
            if(self.heapData[parentNode] > self.heapData[childNode]):
                temp = self.heapData[parentNode]
                self.heapData[parentNode] = self.heapData[childNode]
                self.heapData[childNode] = temp
                
                childNode = parentNode
            else:
                break
    def FindElementAt(self,item,pos,lastNode):
        #initialize result
        result = [False,None]
        #check if current node is the searched one
        if(self.heapData[pos] == item):
            result[0] = True
            result[1] = pos
            return result
        
        checkR = False
        checkL = False
        childNode1 = 2 * pos + 1
        childNode2 = 2 * pos + 2
        #check if left child is present in heap
        if(childNode1 <= lastNode):
            if(self.heapData[childNode1] <= item):
                checkL = True
        #as heap is complete binary tree there is no right node if left is not present
        else:
            return result
        #check if right node is in heap
        if(childNode2 <= lastNode):
            if(self.heapData[childNode2] <= item):
                checkR = True
        
        if(checkL):
            result = self.FindElementAt(item,childNode1,lastNode)
            if(result[0] == True):
                return result
        if(checkR):
            result = self.FindElementAt(item,childNode2,lastNode)
        return result
        
    def FindElement(self,item):
        result = self.FindElementAt(item,0,(len(self.heapData)-1))
        return result    
            
    def DeleteItem(self,item):
        #find the item
        findResult = self.FindElement(item)
        if(findResult[0]==False):
            return
        parentNode = findResult[1]
        #swap item with the last item
        length = len(self.heapData) - 1
        temp = self.heapData[parentNode]
        self.heapData[parentNode] = self.heapData[length]
        self.heapData[length] = temp
        #remove the item to be deleted
        self.heapData.pop()
        length = length - 1                
        #now we have to balance the heap
        child1_Node = 2*(parentNode) + 1
        child2_Node = 2*(parentNode) + 2
        
        while(child1_Node <= length):
            child1 = self.heapData[child1_Node]
            if(child2_Node <= length):
                child2 = self.heapData[child2_Node]
                if(child2 > child1):
                    smallerChildNode = child1_Node
                else:
                    smallerChildNode = child2_Node
            else:
                smallerChildNode = child1_Node
            
            temp = self.heapData[parentNode]
            self.heapData[parentNode] = self.heapData[smallerChildNode]
            self.heapData[smallerChildNode] = temp
            
            parentNode = smallerChildNode
            child1_Node = 2*(parentNode) + 1
            child2_Node = 2*(parentNode) + 2


#use this code if taking input from file
heap = MyHeap()

inArray = [line.rstrip('\n') for line in open('heap_input08.txt')]
#outArray = [line.rstrip('\n') for line in open('heap_input04.txt')]
queryCount = int(inArray[0])
print(inArray)
for commandString in inArray[1:]:
    command =[int(x) for x in commandString.split()]
   
    if(command[0] == 1):
        heap.AddItem(command[1])
    elif(command[0] == 2):
        heap.DeleteItem(command[1])
    elif(command[0] == 3):
        print(heap.MinItem())
#end file input


#queryCountString = input()
#queryCount = int(queryCountString)

#heap = MyHeap()

#for q in range(0,queryCount):
#    commandString = input()
#    command =[int(x) for x in commandString.split()]
#    if(command[0] == 1):
#        heap.AddItem(command[1])
#    elif(command[0] == 2):
#        heap.DeleteItem(command[1])
#    elif(command[0] == 3):
#        print(heap.MinItem())
   
    
    