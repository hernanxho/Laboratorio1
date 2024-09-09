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
            self.root = self.rebalance(self.root)
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
    


    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
            return
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return Node(data, None)
        elif data < node.data:
            node.left = self._insert(node.left, data)
            node.left.parent = node
        elif data > node.data:
            node.right = self._insert(node.right, data)
            node.right.parent = node
        else:
            return node

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.balance_factor(node)

        if balance > 1 or balance < -1:
            node = self.rebalance(node)

        return node
    
    def height(self, node: Optional["Node"]) -> int:
        if node is not None:
            return max(self.height(node.left), self.height(node.right)) + 1
        return 0
    
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
    
    def add_edges(self, node, graph, x=0, y=0, layer=1):
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
        nx.draw(graph, pos, with_labels=True, node_size=3000, node_color="lightgreen", font_size=15, font_weight="bold", arrowsize=20)
        plt.show()


