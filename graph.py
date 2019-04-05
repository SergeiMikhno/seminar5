class Edge:
	def __init__(self, u, v, w):
		self.u = u
		self.v = v
		self.weight = w
		
	def get_weight(self):
		return self.weight
		
	def get_name_edge(self):
		return [self.u.get_name_vertex(), self.v.get_name_vertex()]

class Vertex:
	def __init__(self, key):
		self.vertex = key
		self.neighbors = []
		
	def add_neighbor(self, v):
		assert v not in self.neighbors
		self.neighbors.append(v)
		
	def get_neighbors(self):
		return self.neighbors
		
	def get_name_vertex(self):
		return self.vertex





class Graph:
	def __init__(self):
		self.adjacency_list = dict()
		self.number_of_vertices = 0
		self.number_of_edges = 0
		self.vertices = []
		self.edges = []
		
	def num_vertices(self):
		return self.number_of_vertices
		
	def num_edges(self):
		return self.number_of_edges
		
	def add_vertex(self, v):
		assert v not in self.adjacency_list
		self.adjacency_list[v] = Vertex(v)
		self.vertices.append(Vertex(v))
		self.number_of_vertices += 1
		
	def add_edge(self, u, v, w):
		assert (u in self.adjacency_list) and (v in self.adjacency_list)
		self.adjacency_list[u].add_neighbor(self.adjacency_list[v])
		self.adjacency_list[v].add_neighbor(self.adjacency_list[u])
		self.edges.append(Edge(self.adjacency_list[u], self.adjacency_list[v], w))
		#self.edges.append(Edge(self.adjacency_list[v], self.adjacency_list[u], w))
		self.number_of_edges += 1
		
			
	def contains(self, v):
		return v in self.adjacency_list
		
	def get_edge(self, u, v):
		assert (u in self.adjacency_list) and (v in self.adjacency_list)
		for pair in self.edges:
			if (pair.get_name_edge()[0] == self.adjacency_list[u].get_name_vertex()) and (pair.get_name_edge()[1] == self.adjacency_list[v].get_name_vertex()) \
				or (pair.get_name_edge()[1] == self.adjacency_list[u].get_name_vertex()) and (pair.get_name_edge()[0] == self.adjacency_list[v].get_name_vertex()):
				return pair
				
				
	def get_vertex(self, v):
		assert v in self.adjacency_list
		return self.adjacency_list[v]
			
	def get_vertices(self):
		return self.vertices
		
	def get_edges(self):
		return self.edges
		
	def adj_vertices(self, v):
		return self.adjacency_list[v].get_neighbors()
