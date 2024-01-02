import sys
from Node import Node
import sys
import matplotlib.pyplot as plt
import math
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
class AVL(object):
    def Height(self, root):
        if not root:
            return 0
        return root.height
    def BalanceFactor(self, root):
       if not root:
            return 0
       return self.Height(root.left) - self.Height(root.right)
    def MinValue(self, root):
        if root is None or root.left is None:
            return root
        return self.MinValue(root.left)
    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.value), end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)
    def leftRotate(self, b):
        a = b.right
        T2 = a.left
        a.left = b
        b.right = T2
        b.height = 1 + max(self.Height(b.left),self.Height(b.right))
        a.height = 1 + max(self.Height(a.left),self.Height(a.right))
        return a
    def rightRotate(self, b):
        a = b.left
        T3 = a.right
        a.right = b
        b.left = T3
        b.height = 1 + max(self.Height(b.left),self.Height(b.right))
        a.height = 1 + max(self.Height(a.left),self.Height(a.right))
        return a
    def insert_node(self, root, value):
 
        if not root:
            return Node(value)
        elif value < root.value:
            root.left = self.insert_node(root.left, value)
        else:
            root.right = self.insert_node(root.right, value)
 
        root.height = 1 + max(self.Height(root.left),self.Height(root.right))
 
        balanceFactor = self.BalanceFactor(root)
        if balanceFactor > 1:
            if value < root.left.value:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
 
        if balanceFactor < -1:
            if value > root.right.value:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
 
        return root
    def delete_node(self, root, value):
        if not root:
            return root
        elif value < root.value:
            root.left = self.delete_node(root.left, value)
        elif value > root.value:
            root.right = self.delete_node(root.right, value)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.MinValue(root.right)
            root.value = temp.key
            root.right = self.delete_node(root.right, temp.value)
        if root is None:
            return root
        root.height = 1 + max(self.Height(root.left), self.Height(root.right))
        balanceFactor = self.BalanceFactor(root)
        if balanceFactor > 1:
            if self.avl_BalanceFactor(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.avl_BalanceFactor(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root
    def add_edges(self,graph, node):
     if node is not None:
        if node.left is not None:
            graph.add_edge(node.value, node.left.value)
            self.add_edges(graph, node.left)
        if node.right is not None:
            graph.add_edge(node.value, node.right.value)
            self.add_edges(graph, node.right)        
    def plot_tree(self,root):
        graph = nx.DiGraph()
        self.add_edges(graph, root)
        pos = graphviz_layout(graph, prog='dot')
        nx.draw(graph, pos, with_labels=True, arrows=False)
        plt.show()

