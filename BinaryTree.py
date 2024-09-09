from Node import *
from typing import Any, Optional, Tuple
import Lectura as le
import networkx as nx
import matplotlib.pyplot as plt

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
    
    def insert(self, node: Optional ["Node"], data):
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
        # Actualizar el factor de balance y balancear el nodo después de la inserción
            self.updateFactor(node)
            return self.balance(node, data)

    def balance(self, node, data):
        if node is None:
            return None

        nodeBF = node.balanceFactor

        # Balanceamos el árbol de acuerdo con el factor de balance
        if nodeBF < -1:  # Si está desbalanceado hacia la izquierda
            if data < node.left.data:  # Rotación simple a la derecha
                return self.simpleRightRotation(node)
            else:  # Rotación doble izquierda-derecha
                return self.doubleLeftRightRotation(node)

        if nodeBF > 1:  # Si está desbalanceado hacia la derecha
            if data > node.right.data:  # Rotación simple a la izquierda
                return self.simpleLeftRotation(node)
            else:  # Rotación doble derecha-izquierda
                return self.doubleRightLeftRotation(node)

        return node

    def simpleRightRotation(self, node):
        aux = node.left
        node.left = aux.right
        aux.right = node
        self.updateFactor(node)
        self.updateFactor(aux)
        return aux

    def simpleLeftRotation(self, node):
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
    
    def add_edges(self, node, graph, pos=None, x=0, y=0, layer=1):
        if node is None:
            return
        
        graph.add_node(node.data, pos=(x, y))
        
        if node.left is not None:
            graph.add_edge(node.data, node.left.data)
            self.add_edges(node.left, graph, x=x - 1 / layer, y=y - 1, layer=layer + 1)
        
        if node.right is not None:
            graph.add_edge(node.data, node.right.data)
            self.add_edges(node.right, graph, x=x + 1 / layer, y=y - 1, layer=layer + 1)

    def draw_tree(self, root):
        graph = nx.DiGraph()
        self.add_edges(root, graph)

        pos = nx.get_node_attributes(graph, 'pos')
        nx.draw(graph, pos, with_labels=True, node_size=3000, node_color="lightgreen", font_size=15, font_weight="bold", arrows=False)
        plt.show()


