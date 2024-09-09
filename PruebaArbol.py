from BinaryTree import *
from Node import Node

tree=BinaryTree()
#CLASE PARA FUNCIONAMIENTO DE LOS NODOS EN EL ARBOL
def printRoot(node):
    if(node!=None):
     print(node.data)
     printRoot(node.left)
     printRoot(node.right)