from BinaryTree import *
from Node import Node
import Lectura as le

tree=BinaryTree()

def printRoot(node):
    if(node!=None):
     print(node.data)
     printRoot(node.left)
     printRoot(node.right)

def encontrarNodo(node,data):
   if(node!=None):
     if(node.data.lower()==data.lower()):
      print("pelicula encontrada "+node.data)
     encontrarNodo(node.left,data)
     encontrarNodo(node.right,data)



