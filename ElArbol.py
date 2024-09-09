from BinaryTree import *
from Node import Node
import Lectura as le

tree=BinaryTree()

def printRoot(node):
    if(node!=None):
     print(node.data)
     printRoot(node.left)
     printRoot(node.right)




