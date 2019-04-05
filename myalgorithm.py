def Dijkstra(s, graph):
	n = graph.num_vertices()
	p = [s]*n
	min_dist = [1000000]*n
	used = [0]*n
	min_dist[s] = 0
	
	
	while 0 in used:
		u = -1
		min_d = 1000000
		for i in range(n):
			if used[i] == 0 and min_dist[i] < min_d:
				min_d = min_dist[i]
				u = i
	
		for v in graph.adj_vertices(u):
			j = v.get_name_vertex()
			if min_dist[u] + graph.get_edge(u, j).get_weight() < min_dist[j]:
				min_dist[j] = min_dist[u] + graph.get_edge(u, j).get_weight()
				p[j] = u
		used[u] = 1
	return p

