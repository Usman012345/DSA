import networkx as nx
import sys
from graph import graph
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt
sys.setrecursionlimit(60000)
class kruskal:
    def __init__(self,root):
        self.root=root
        self.weight=0
    def cut_min_spanning(self):
        if self.root.neighbours is None:
            return
        if self.root.neighbours!=None:
            x=self.root.neighbours[0]
            for y in self.root.neighbours:
                if x.weight>y.weight:
                    x=y.weight
            if x.status=="Unvisited":
                self.weight+=x.weight
                self.plot_graph(self.root)
                cut_min_spanning(x)
            else:
                del(x)
                self.cut_min_spanning()
    def add_edges(self,graph_, node):
     if node is not None:
        flag= graph.visited.get_node(node.data)
        if flag==None:
            self.visited.insert_first(node)
            node.status="intraversal"
            if node.next is not None:
                graph_.add_edge(node.data, node.next.data)
                if node.neighbours is not None:
                    for x in node.neighbours:
                        graph_.add_edge(node.data,x.data)
                        if x.neighbours is not None:
                            for y in x.neighbours:
                                graph_.add_edge(x.data,y.data)
                node.status="traversed"
                self.add_edges(graph_, node.next) 
    def plot_graph(self,root):
        graph = nx.DiGraph()
        self.add_edges(graph, root)
        pos = graphviz_layout(graph, prog='dot')
        nx.draw(graph, pos, with_labels=True, arrows=False)
        plt.show()        
            
            

