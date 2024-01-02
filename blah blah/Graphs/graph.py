import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt
class graph(object):
    def __init__(self,list_,list_1,list_2):
        self.vertices=list_
        self.kruskal_list=list_
        self.visited=list_1
    def DFS(self,root):
        self.plot_graph(root,"DFS")
    def BFS(self,root):
        self.plot_graph(root,"BFS")
    def kruskal(self,root):
        self.plot_graph(root,"kruskal")
    def add_edges(self,graph, node):
     if node is not None:
        flag= self.visited.get_node(node.data)
        if flag==None:
            self.visited.insert_first(node)
            node.status="intraversal"
            if node.next is not None:
                graph.add_edge(node.data, node.next.data)
                if node.neighbours is not None:
                    for x in node.neighbours:
                        graph.add_edge(node.data,x.data)
                        if x.neighbours is not None:
                            for y in x.neighbours:
                                graph.add_edge(x.data,y.data)
                node.status="traversed"
                self.add_edges(graph, node.next)          
    def add_edges_BFS(self,graph, node):
     if node is not None:
        flag= self.visited.get_node(node.data)
        if flag==None:
            self.visited.insert_first(node)
            node.status="intraversal"
            if node.next is not None:
                graph.add_edge(node.data, node.next.data)
                self.add_edges(graph, node.next)
                if node.neighbours is not None:
                    for x in node.neighbours:
                        graph.add_edge(node.data,x.data)
                        if x.neighbours is not None:
                            for y in x.neighbours:
                                graph.add_edge(x.data,y.data)
                node.status="traversed"
                self.add_edges(graph, node.next)
    def add_edges_Kruskal(self,graph, node):
      if node is not None:
        flag= self.visited.get_node(node.data)
        if flag==None:
            self.visited.insert_first(node)
            node.status="intraversal"
            if node.next is not None:
                graph.add_edge(node.data, node.next.data)
                if node.neighbours is not None:
                    for x in node.neighbours:
                        graph.add_edge(node.data,x.data)
                        if x.neighbours is not None:
                            for y in x.neighbours:
                                graph.add_edge(x.data,y.data)
                node.status="traversed"
                self.add_edges(graph, node.next) 
    def plot_graph(self,root,Type):
        graph = nx.DiGraph()
        if Type=="DFS":
            self.add_edges(graph, root)
        if Type=="BFS":
            self.add_edges_BFS(graph, root)
        if Type=="kruskal":
            self.add_edges_Kruskal(graph, root)
        pos = graphviz_layout(graph, prog='dot')
        nx.draw(graph, pos, with_labels=True, arrows=False)
        plt.show()
    def cut_min_spanning(self,root):
        if self.root.next is None:
            self.kruskal_list.insert_first(root)
            return
        if self.root.neighbours!=None:
            x=self.root.neighbours[0]
            for y in self.root.neighbours:
                if x.weight>y.weight:
                    x=y.weight
            if x.status=="Unvisited":
                self.kruskal_list.insert_first(x)
                self.weight+=x.weight
            else:
                self.kruskal_list.remove_node(x.data)
                self.cut_min_spanning(root)
        self.plot_graph(kruskal_list.head,"kruskal")



