from Node import Node
from RedBlacktree import RedBlacktree
import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
obj = RedBlacktree()
obj.insert(70)
obj.insert(60)
obj.insert(85)
obj.insert(80)
obj.insert(95)
obj.insert(65) 
obj.print_tree()
print("\nAfter deleting an element")
obj.delete_node(80)
obj.print_tree()
obj.plot_tree(obj.root)
