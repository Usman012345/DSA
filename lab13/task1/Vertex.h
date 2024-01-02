#pragma once
#include <iostream>
#include<vector>
using namespace std;
class Vertex
{
public:
	vector<Vertex> in_neighbours;
	vector<Vertex> out_neighbours;
	string value;
	int* intime;
	int* outtime;
	string status="unvisited";

	bool has_in_neighbour()
	{
		return in_neighbours.empty();
	}
	bool has_out_neighbours()
	{
		return out_neighbours.empty();
	}
	bool has_neighbours()
	{
		bool one = in_neighbours.empty();
		bool two = out_neighbours.empty();
		if (one || two)
			return true;
		else
			return false;
	}
	vector<Vertex> get_in_neighbours()
	{
		return in_neighbours;
	}
	vector<Vertex> get_out_neightbours()
	{
		return out_neighbours;
	}
	void add_in_neighbour(Vertex vect)
	{
		in_neighbours.push_back(vect);
	}
	void add_out_neighbour(Vertex vect)
	{
		out_neighbours.push_back(vect);
	}
	

};

