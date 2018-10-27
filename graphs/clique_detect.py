import ER_gen
import numpy as np

def find_clique(n, p, seed):

	ER_gen.seed_init(seed)
	VlessS = ER_gen.random_graph_list(n, p)
	S = set()

	def delete_vertex(j):
		adj_vert = VlessS[j]
		for x in adj_vert:
			VlessS[x].remove(j)
		del VlessS[j]


	while len(VlessS) > 0:
		v = np.random.choice([x for x in VlessS.keys()])
		S.add(v)
		v_neigh = VlessS[v]

		toDelete =[]
		for x in VlessS.keys():
			if x not in v_neigh:
				toDelete += [x]

		for x in toDelete:
			delete_vertex(x)

	return S


def find_clique_input_and_print(adj_list):
	VlessS = adj_list
	S = set()

	def delete_vertex(j):
		adj_vert = VlessS[j]
		for x in adj_vert:
			VlessS[x].remove(j)
		del VlessS[j]

	G = list_to_plot(VlessS)
	graph_draw(G, vertex_text = G.vertex_index, vertex_font_size=18,
			output_size = (200, 200), output="two-nodes0.png")
	i = 1

	while len(VlessS) > 0:
		v = np.random.choice([x for x in VlessS.keys()])
		S.add(v)
		v_neigh = VlessS[v]

		toDelete =[]
		for x in VlessS.keys():
			if x not in v_neigh:
				toDelete += [x]

		for x in toDelete:
			delete_vertex(x)

		G = list_to_plot(VlessS)
		graph_draw(G, vertex_text = G.vertex_index, vertex_font_size=18,
			output_size = (200, 200), output="two-nodes" + str(i) + ".png")

		i += 1

	return S


