import sys
from Node import Node
import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
from AVL import AVL
obj= AVL()
root = None
root = obj.insert_node(root,4)
root = obj.insert_node(root,6)
root = obj.insert_node(root,5)
root = obj.insert_node(root,7)
obj.plot_tree(root)
print("PREORDER")
obj.preOrder(root)
obj.delete_node(root,6)
print("\ndeleting 6")
obj.preOrder(root)
print("\n left rotate")
b=obj.insert_node(root,9)
obj.leftRotate(b)
obj.preOrder(root)
print("\n right rotate")
obj.rightRotate(b)
obj.preOrder(root)
print("\n")

