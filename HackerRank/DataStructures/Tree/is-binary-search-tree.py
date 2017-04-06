# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/is-binary-search-tree
@author: nandu
"""
""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""

def check_binary_search_tree_(root):
    return checkBST(root,-1,10001)
    
def checkBST(node,minNode,maxNode):
    
    #if we have reached end of leaf
    if(not(node)):
        return True
        
    #if current node violates BST rule
    if((node.data >= maxNode) or (node.data <= minNode)):
        return False
    
    #when going to left sub tree, the nodes in it should be 
    #less than current nodes value
    if(checkBST(node.left,minNode,node.data)):
        #when going to right sub tree, the nodes in it should be 
        #greater than current nodes value
        return (checkBST(node.right,node.data,maxNode))
    else:
        return False
    