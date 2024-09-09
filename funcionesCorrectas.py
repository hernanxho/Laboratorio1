import networkx as nx
import matplotlib.pyplot as plt

class Node:
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

    def balance_factor(self, node):
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

    def rebalance(self, node):
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

    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, node, data):
        if node is None:
            return node
        elif data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
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

        if node is None:
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

avl_tree = AVLTree()
#avl_tree.insert(5)
#avl_tree.insert(3)
#avl_tree.insert(7)
#avl_tree.insert(2)
#avl_tree.insert(4)
#avl_tree.insert(6)
#avl_tree.insert(8)

#avl_tree.draw_tree(avl_tree.root)

#avl_tree.delete(4)
#avl_tree.draw_tree(avl_tree.root)