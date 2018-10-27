from graph_tool.all import *

def list_to_graph(adj_list):
	G = Graph(directed = False)

	V = {}
	for i in range(len(adj_list)):
		V[i] = G.add_vertex()

	E = {}
	for k in adj_list.keys():
		for v in adj_list[k]:
			E[(k, v)] = G.add_edge(k, v)

	return G

def list_to_plot(adj_list):
	G = Graph(directed = False)

	V = {}
	for i in range(len(adj_list)):
		V[i] = G.add_vertex()

	E = {}
	for k in adj_list.keys():
		for v in adj_list[k]:
			if (v, k) in E:
				continue
			E[(k, v)] = G.add_edge(k, v)

	return G

	graph_draw(G, vertex_text = g.vertex_index, vertex_font_size=18,
		output_size = (200, 200), output = "two-nodes.png")

