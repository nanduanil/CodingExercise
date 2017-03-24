# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 15:34:33 2017
problem : https://www.hackerrank.com/challenges/qheap1
@author: nanil
"""

#%%
import math
class MyHeap():
    
    def __init__(self):
        self.heapData = [] #heap data
        self.heapTrack = {} #track location of each item on heap
        #self.outData = []    
        
    def MinItem(self):
        #self.outData.append(self.heapData[0])
        return self.heapData[0]
    
    def AddItem(self,item):
        self.heapData.append(item)
        childNode = len(self.heapData) - 1
        self.heapTrack[item] = childNode
        while(childNode > 0):
            parentNode = math.ceil(childNode/2) - 1
            if(self.heapData[parentNode] > self.heapData[childNode]):
                temp = self.heapData[parentNode]
                self.heapData[parentNode] = self.heapData[childNode]
                self.heapData[childNode] = temp
                #change heap tracking as items have been swapped
                self.heapTrack[self.heapData[childNode]] = childNode
                self.heapTrack[self.heapData[parentNode]] = parentNode
                
                childNode = parentNode
            else:
                break
    
    def DeleteItem(self,item):
        #find the item
        parentNode = self.heapTrack[item]
        #swap item with the last item
        length = len(self.heapData) - 1
        temp = self.heapData[parentNode]
        self.heapData[parentNode] = self.heapData[length]
        self.heapData[length] = temp
        #change heap tracking as items have been swapped
        self.heapTrack[self.heapData[length]] = length
        self.heapTrack[self.heapData[parentNode]] = parentNode
        #remove the item to be deleted
        self.heapData.pop()
        del self.heapTrack[item]
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
            
            #if parent is already smaller then exit
            if(self.heapData[smallerChildNode] > self.heapData[parentNode]):
                break            
            temp = self.heapData[parentNode]
            self.heapData[parentNode] = self.heapData[smallerChildNode]
            self.heapData[smallerChildNode] = temp
            #change heap tracking as items have been swapped
            self.heapTrack[self.heapData[smallerChildNode]] = smallerChildNode
            self.heapTrack[self.heapData[parentNode]] = parentNode
            
            parentNode = smallerChildNode
            child1_Node = 2*(parentNode) + 1
            child2_Node = 2*(parentNode) + 2

queryCountString = input()
queryCount = int(queryCountString)
heap = MyHeap()
for q in range(0,queryCount):
    commandString = input()
    command =[int(x) for x in commandString.split()]
    if(command[0] == 1):
        heap.AddItem(command[1])
    elif(command[0] == 2):
        heap.DeleteItem(command[1])
    elif(command[0] == 3):
        print(heap.MinItem())
        
#==============================================================================
# #use this code if taking input from file
# heap = MyHeap()
# 
# inArray = [line.rstrip('\n') for line in open('C:\\Users\\nanil\\Desktop\\Algo\\HackerRank\\Heap\\heap_input09.txt')]
# #outArray = [line.rstrip('\n') for line in open('heap_input04.txt')]
# queryCount = int(inArray[0])
# #print(inArray)
# for commandString in inArray[1:]:
#     command =[int(x) for x in commandString.split()]
#    
#     if(command[0] == 1):
#         heap.AddItem(command[1])
#     elif(command[0] == 2):
#         heap.DeleteItem(command[1])
#     elif(command[0] == 3):
#         print(heap.MinItem())
# #end file input
#==============================================================================



   
    
    