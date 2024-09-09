import networkx as nx
import matplotlib.pyplot as plt
from typing import Any, Optional, Tuple
from tkinter import messagebox
import Node
#CLASE PARA LA GENERACION DEL ARBOL
class Node: #FUNCION ESTEROTIPICA NODO
    def __init__(self, data, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        else:
            return node.height

    def update_height(self, node): 
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def balance_factor(self, node): #ACTUALIZAR FACTOR DE BALANCEO
        return self.height(node.right) - self.height(node.left)

    def simple_left_rotation(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        self.update_height(z)
        self.update_height(y)
        return y

    def simple_right_rotation(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        self.update_height(z)
        self.update_height(y)
        return y

    def rebalance(self, node): #BALANCEO
        balance = self.balance_factor(node)
        if balance > 1:
            if self.height(node.right.right) >= self.height(node.right.left):
                node = self.simple_left_rotation(node)
            else:
                node.right = self.simple_right_rotation(node.right)
                node = self.simple_left_rotation(node)
        elif balance < -1:
            if self.height(node.left.left) >= self.height(node.left.right):
                node = self.simple_right_rotation(node)
            else:
                node.left = self.simple_left_rotation(node.left)
                node = self.simple_right_rotation(node)
        return node

    def insert(self, data): #INSERCION
        if(data==""):
         return 
        if self.root is None:
            self.root = Node(data, None)
            return
        self.root = self._insert(self.root, data)

    def _insert(self, node, data): #INSERCION CASOS
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

    def delete(self, data): #BORRAR
        self.root = self._delete(self.root, data)

    def _delete(self, node, data): #BORRAR CASOS
        if node is None:
            return node
        elif data.lower() < node.data.lower():
            node.left = self._delete(node.left, data)
        elif data.lower() > node.data.lower():
            node.right = self._delete(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_node = self.find_min(node.right)
                node.data = min_node.data
                node.right = self._delete(node.right, min_node.data)

        if node is None: #SI NODO ES VACIO
            return node

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.balance_factor(node)

        if balance > 1 or balance < -1:
            node = self.rebalance(node)

        return node

    def find_min(self, node):
        while node.left is not None:
            node = node.left
        return node
    
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


    def search(self, data: Any) -> Tuple[Optional["Node.Node"], Optional["Node.Node"]]: #BUSQUEDA DE DATA
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
    def uncle (self, node):
        p,pad = self.search(node.data)
        if pad is None:
            return
        pad, gf = self.search(pad.data)
        if gf is None:
            return None
        if pad is gf.left:
            return gf.right
        else:
            return gf.left

    def grandfather(self,node): #FUNCION ABUELO
        p,pad = self.search(node.data)
        if pad is None:
            return
        pad, gf = self.search(pad.data)
        return gf

    def father (self, node): #FUNCION PADRE
        p,pad = self.search(node.data)
        return pad
    
    def recorrido_niveles(self,node: Optional["Node"],b,p,q)->None: #RECORRIDO POR NIVELES
      if node is not None:
        if(node == self.root):
          p.append(node)
          q.append(b)
        if(node.left!=None and node.right!=None):
          p.append(node.left)
          q.append(b+1)
          p.append(node.right)
          q.append(b+1)
        elif(node.left!=None and node.right==None):
          p.append(node.left)
          q.append(b+1)
        elif(node.right!=None and node.left==None):
          p.append(node.right)
          q.append(b+1)
        self.recorrido_niveles(node.left,b+1,p,q)
        self.recorrido_niveles(node.right,b+1,p,q)
        
    def mostrarNiveles(self, root): #RESULTADO DEL RECORRIDO POR NIVELES
        p = []
        q = []
        message = ""
        if root is None:
            message = "No hay árbol por recorrer"
        else:
            self.recorrido_niveles(root, 0, p, q)
            for i in range(len(p)):
                message = message + p[i].data + ", "
        messagebox.showinfo("Niveles del Árbol", message)
        
    def familiar(self,data): #CASOS FAMILIARES AL NODO
        p,pad=self.search(data)
        if(p==None):
            return
        uncle = self.uncle(p)
        grandfather=self.grandfather(p)
       
        if(pad==None):
            padre=" Es huérfano"
        else:
            padre=pad.data
       
        if(uncle==None):
            tio=" No tiene"
        else:
            tio=uncle.data
       
        if(grandfather==None):
            abuelo="No tiene"
        else:
            abuelo = grandfather.data
        listNodos=[]
        listNiveles=[]
        self.recorrido_niveles(self.root,0,listNodos,listNiveles)
        level=listNiveles[listNodos.index(p)]
        messagebox.showinfo("Datos","Los datos de -" + p.data + "- son: \nPadre: " 
                            + padre + "\nAbuelo: "+ abuelo + "\nTio: " +tio+ "\nNivel: " +str(level)+ "\nFactor de balanceo: " +str(self.balance_factor(p)) )

    
    #GENERACION DEL ARBOL
avl_tree = AVLTree()

