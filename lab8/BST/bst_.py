from Node import Node
import matplotlib.pyplot as plt
import math
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
class bst_(object):
    """description of class"""
    def __init__(self):
        self.root=None
    def insert(self,root,data):
        if root ==None:
            root=Node(data)
            return root
        elif data<root.data:
            root.left=self.insert(root.left,data)
        elif data>root.data:
            root.right=self.insert(root.right,data)
        return root
    def gettree(self):
        return self.root
    def findNode(self,root,val):
        if  root==None:
            return False
        elif val==root.data:
            return True
        elif val<root.data:
            return findNode(root.left,val)
        elif val>root.data:
            return findNode(root.right,val)
    
    def successor(self,root):
        min=root.data
        while root.left:
            min=root.left.data
            root=root.left
        return min

    def delete_node(self,root,val):
        if root==None:
            return root
        if val<root.data:
            root.left = self.delete_node(root.left, val)
        elif val>root.data:
            root.right=self.delete_node(root.right,value)
        else:
            if root.left==None:
                return root.right
            elif root.right==None:
                return root.left
            #temp=root.right
            #min=temp.data
            #while temp.left:
             #   temp=temp.left
              #  min=temp.data
            root.data=self.successor(root.right)
            root.right=self.delete_node(root.right,root.data)
        return root
    def preOrder(self,root): 
        if root==None: 
            return      
        print(root.data)
        self.preOrder(root.left) 
        self.preOrder(root.right)
    def inOrder(self,root): 
        if root==None: 
            return      
        self.inOrder(root.left)
        print(root.data)
        self.inOrder(root.right)    
    def postOrder(self,root): 
        if root==None: 
            return      
        self.preOrder(root.left) 
        self.preOrder(root.right)
        print(root.data)
    def count_nodes(self,root):
        if root==None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)
    def height(self,root):
        x=self.count_nodes(root)
        return (math.log2(x+1))-1
    def print_leaf(self,root):
        if root==None: 
            return
        if root.left==None and root.right==None:
            print(root.data)
        self.print_leaf(root.left) 
        self.print_leaf(root.right)
    def add_edges(self,graph, node):
     if node is not None:
        if node.left is not None:
            graph.add_edge(node.data, node.left.data)
            self.add_edges(graph, node.left)
        if node.right is not None:
            graph.add_edge(node.data, node.right.data)
            self.add_edges(graph, node.right)        
    def plot_tree(self,root):
        graph = nx.DiGraph()
        self.add_edges(graph, root)
        pos = graphviz_layout(graph, prog='dot')
        nx.draw(graph, pos, with_labels=True, arrows=False)
        plt.show()
    def checkBST(self,root):
        if root.left == None and root.right == None:
            return True
        if root == None:
            return True
        if root.left != None:
            if root.left.data < root.data:
                return True
            else:
                return False
        if root.right != None:
            if root.right.data > root.data:
                return True
            else:
                return False
        return self.checkBST(root.left) and self.checkBST(root) and self.checkBST(root.right)
