
from Node import *
from typing import Any, Optional, Tuple
import Lectura as le

class BinaryTree:

    def __init__(self, root : Optional["Node"]  = None) -> None:
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

    def insert(self, node: Optional["Node"] , data: Any) -> "Node":
        if le.encontrar(data) == "":
            print("Definitivamente no encontrado")
        else:
            if node is None:
                nuevoNodo = Node(data)
                if self.root is None:
                    self.root = nuevoNodo

                return nuevoNodo

            if data < node.data:
                node.left = self.insert(node.left, data)
            elif data > node.data:
                node.right = self.insert(node.right, data)
            else:
                return node

            self.updateFactor(node)
            nodeBF = node.balanceFactor

            if nodeBF < -1 and data < node.left.data:
                return self.simpleRightRotation(node)
            if nodeBF > 1 and data > node.right.data:
                return self.simpleLeftRotation(node)
            if nodeBF < -1 and data > node.left.data:
                return self.doubleLeftRightRotation(node)
            if nodeBF > 1 and data < node.right.data:
                return self.doubleRightLeftRotation(node)


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
            return True
        return False

    def __pred(self, node: "Node") -> Tuple["Node", "Node", Optional["Node"]]:
        p, pad = node.left, node
        while p.right is not None:
            p, pad = p.right, p
        return p, pad, p.left

    def __sus(self, node: "Node") -> Tuple["Node", "Node", Optional["Node"]]:
        p, pad = node.right, node
        while p.left is not None:
            p, pad = p.left, p
        return p, pad, p.right

    def preorder(self) -> None:
        self.__preorder_r(self.root)
        print()

    def __preorder_r(self, node: Optional["Node"]) -> None:
        if node is not None:
            print(node.data, end=' ')
            self.__preorder_r(node.left)
            self.__preorder_r(node.right)

    def preorder_nr(self) -> None:
        s = []
        p = self.root
        while p is not None or len(s) > 0:
            if p is not None:
                print(p.data, end=' ')
                s.append(p)
                p = p.left
            else:
                p = s.pop()
                p = p.right
        print()

    def inorder(self) -> None:
        self.__inorder_r(self.root)
        print()

    def __inorder_r(self, node: Optional["Node"]) -> None:
        if node is not None:
            self.__inorder_r(node.left)
            print(node.data, end=' ')
            self.__inorder_r(node.right)

    def inorder_nr(self) -> None:
        s = []
        p = self.root
        while p is not None or len(s) > 0:
            if p is not None:
                s.append(p)
                p = p.left
            else:
                p = s.pop()
                print(p.data, end=' ')
                p = p.right
        print()

    def postorder(self) -> None:
        self.__postorder_r(self.root)
        print()

    def __postorder_r(self, node: Optional["Node"]) -> None:
        if node is not None:
            self.__postorder_r(node.left)
            self.__postorder_r(node.right)
            print(node.data, end=' ')

    def levels_nr(self) -> None:
        q = []
        p = self.root
        q.append(p)
        while len(q) > 0:
            p = q.pop(0)
            print(p.data, end=' ')
            if p.left is not None:
                q.append(p.left)
            if p.right is not None:
                q.append(p.right)
        print()

    def height(self, node: Optional["Node"]) -> int:
        return self.__height_r(node)

    def __height_r(self, node: Optional["Node"]) -> int:
        if node is None:
            return 0
        return 1 + max(self.__height_r(node.left), self.__height_r(node.right))
    
    def search(self, data: Any) -> Tuple[Optional["Node"], Optional["Node"]]:
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

        return p, pad

    def updateFactor(self, node):
        if node is not None:
            node.balanceFactor = (node.height(node.right) - node.height(node.left))



    def simpleRightRotation(self, node:Node):
        aux = node.left
        node.left = aux.right
        aux.right = node
        return aux

    def simpleLeftRotation(self, node:Node):
        aux = node.right
        node.right = aux.left
        aux.left = node
        return aux

    def doubleRightLeftRotation(self, node):
        node.right = self.simpleRightRotation(node.right)
        return self.simpleLeftRotation(node)

    def doubleLeftRightRotation(self, node):
        node.left = self.simpleLeftRotation(node.left)
        return self.simpleRightRotation(node)

    def uncle (self, node):
        p,pad = self.search(node)
        if pad is None:
            return
        pad, gf = self.search(pad.data)
        if gf is None:
            return None
        if pad is gf.left:
            return gf.right
        else:
            return gf.left

    def grandfather(self,node):
        p,pad = self.search(node)
        if pad is None:
            return
        pad, gf = self.search(pad.data)
        return gf

    def father (self, node):
        p,pad = self.search(node)
        return pad


