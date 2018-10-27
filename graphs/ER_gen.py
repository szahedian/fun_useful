import numpy as np

def seed_init(seed):
	np.random.seed(seed)

def random_graph_matrix(n, p):
	adj_mat = np.zeros((n, n))
	for i in range(n):
		samples = np.random.random((n - i, ))
		samples = [1 if (x > p) else 0 for x in (samples < p)]
		adj_mat[i, i:] = samples
		adj_mat[i:, i] = samples
	return adj_mat

def random_graph_list(n, p):
	matrix = random_graph_matrix(n, p)
	adj_list = {}
	for i in range(n):
		for j in range(n):
			if i == j:
				continue
			if matrix[i, j]:
				if i not in adj_list:
					adj_list[i] = [j]
				else:
					adj_list[i] += [j]
	return adj_list

def list_from_matrix(matrix):
	adj_list = {}
	n = matrix.shape[0]
	for i in range(n):
		for j in range(n):
			if matrix[i, j]:
				if i not in adj_list:
					adj_list[i] = [j]
				else:
					adj_list[i] += [j]
	return adj_list

