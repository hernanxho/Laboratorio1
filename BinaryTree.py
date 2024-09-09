from Node import *
from typing import Any, Optional, Tuple
import Lectura as le

class BinaryTree:

    def __init__(self, root: Optional["Node.Node"] = None) -> None:
        self.root = root

    def levels_nr(self) -> None:
        q = []
        p = self.root
        q.append(p)
        while len(q) > 0:
            p = q.pop(0)
            print(p.data, end = ' ')
            if p.left is not None:
                q.append(p.left)
            if p.right is not None:
                q.append(p.right)
        print()
    
    def insert(self, data: Any) -> bool:
     if(le.encontrar(data)==""):
         print("Definitivamente no encontrado")
     else:
         to_insert = Node(data)
         if self.root is None:
             self.root = to_insert
             return True
         else:
            p, pad = self.search(data)
            if p is not None:
                return False
            else:
                if data < pad.data:
                    pad.left = to_insert
                else:
                    pad.right = to_insert
                self.balance(self.root,data)
                return True

    def delete(self, data: Any, mode: bool = True) -> bool:
        p, pad = self.search(data)
        if p is not None:
            if p.left is None and p.right is None:
                if pad is None:
                    self.root = None
                elif p == pad.left:
                    pad.left = None
                else:
                    pad.right = None
                del p
            elif p.left is None and p.right is not None:
                if pad is None:
                    self.root = p.right
                elif p == pad.left:
                    pad.left = p.right
                else:
                    pad.right = p.right
                del p
            elif p.left is not None and p.right is None:
                if pad is None:
                    self.root = p.left
                elif p == pad.left:
                    pad.left = p.left
                else:
                    pad.right = p.left
                del p
            else:
                if mode:
                    pred, pad_pred, son_pred = self.__pred(p)
                    p.data = pred.data
                    if p == pad_pred:
                        pad_pred.left = son_pred
                    else:
                        pad_pred.right = son_pred
                    del pred
                else:
                    sus, pad_sus, son_sus = self.__sus(p)
                    p.data = sus.data
                    if p == pad_sus:
                        pad_sus.right = son_sus
                    else:
                        pad_sus.left = son_sus
                    del sus
            self.balance(self.root,data)
            return True
        return False
    
    def search(self, data: Any) -> Tuple[Optional["Node.Node"], Optional["Node.Node"]]:
        p, pad = self.root, None 
        while p is not None:
            if data.lower() == p.data.lower():
                return p, pad
            else:
                pad = p
                if data.lower() < p.data.lower():
                    p = p.left
                else:
                    p = p.right
        if(p is None):
         print("No se encontró")
        return p, pad
    
    def balance(self, node: Optional["Node"], data) -> Optional["Node"]:
        if node is None:
            return None

        
        nodeBF = node.balanceFactor

       
        if nodeBF < -1:
            if data < node.left.data: 
                return self.simpleRightRotation(node)
            else:  
                return self.doubleLeftRightRotation(node)

       
        if nodeBF > 1:
            if data > node.right.data:  
                return self.simpleLeftRotation(node)
            else:  
                return self.doubleRightLeftRotation(node)

        return node  

    def simpleRightRotation(self, node: "Node") -> "Node":
        aux = node.left
        node.left = aux.right
        aux.right = node

        
        self.updateFactor(node)
        self.updateFactor(aux)

        return aux

    def simpleLeftRotation(self, node: "Node") -> "Node":
        aux = node.right
        node.right = aux.left
        aux.left = node

        
        self.updateFactor(node)
        self.updateFactor(aux)

        return aux

    def doubleRightLeftRotation(self, node: "Node") -> "Node":
        node.right = self.simpleRightRotation(node.right)
        return self.simpleLeftRotation(node)

    def doubleLeftRightRotation(self, node: "Node") -> "Node":
        node.left = self.simpleLeftRotation(node.left)
        return self.simpleRightRotation(node)

    def updateFactor(self, node: "Node") -> None:
        if node is not None:
            
            node.balanceFactor = self.height(node.right) - self.height(node.left)

    def height(self, node: Optional["Node"]) -> int:
        if node is None:
            return -1  
        return max(self.height(node.left), self.height(node.right)) + 1
    
    def __pred(self, node: "Node") -> Tuple["Node", "Node", Optional["Node"]]:
        p, pad = node.left, node
        while p.right is not None:
            p, pad = p.right, p
        return p, pad, p.left

    def __sus(self, node: "Node") -> Tuple["Node", "Node", Optional["Node"]]:
        p, pad = node.right, node
        while p.left is not None:
            p, pad = p.left, p
        return p,pad,p.right