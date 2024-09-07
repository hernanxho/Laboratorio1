from BinaryTree import *
from Node import Node

tree=BinaryTree()

def printRoot(node):
    if(node!=None):
     print(node.data)
     printRoot(node.left)
     printRoot(node.right)

