#pragma once
#include <iostream>
#include<vector>
#include"Vertex.h"
class Graph
{
public:
	vector<Vertex> vertices;
	void add_vertex(Vertex v)
	{
		vertices.push_back(v);
	}
	void add_di_edge(Vertex v, Vertex u)
	{
		v.add_out_neighbour(u);
		u.add_in_neighbour(v);
	}
	void add_bi_edges(Vertex u, Vertex v)
	{
		add_di_edge(u, v);
		add_di_edge(v, u);
	}
	void get_edges()
	{
		int i = 0;
		vector<Vertex>	ret;
		for (i = 0;i <= vertices.size();i++)
		{
			for (int x = 0;x <= vertices[i].out_neighbours.size();x++)
			{
				Vertex v = vertices[i];
				Vertex u = vertices[i].out_neighbours[x];
				ret.push_back(v, u);
			}
		}
	}



};

