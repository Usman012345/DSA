from linklist import linklist
from Node import Node_
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt
from graph import graph
from kruskal_algorithm import kruskal


list_=linklist()
list_1=linklist()
list_2=linklist()
list_.insert_last('a')
list_.insert_last('b')
list_.insert_first('c')
list_.insert_first('d')
list_.insert_index('g', 2)
root=list_.head
node1=Node_("0")
node2=Node_("2")
node3=Node_("9")
node4=Node_("Blah")
c_node=list_.get_node("c")
b_node=list_.get_node("b")
c_node.neighbours.append(node1)
c_node.neighbours.append(node2)
c_node.neighbours.append(node4)
c_node.neighbours.append(node3)
node3.neighbours.append(b_node)
obj=graph(list_,list_1,list_2)
obj.DFS(root)
obj.visited.head=None
obj.BFS(root)


