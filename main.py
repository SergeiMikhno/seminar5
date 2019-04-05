from graph import Graph, Vertex, Edge
from myalgorithm import Dijkstra

g = Graph()

with open("graph_33.txt","r") as f:
	line = f.readline()
	n = list(map(int,line.split()))[0]
	m = list(map(int,line.split()))[1]
	for i in range(m):
		g.add_vertex(i)
	count = 0
	while count < n:
		line = list(map(int,f.readline().split()))
		pair = []
		for i in range(m):
			if line[i] == 1:
				pair.append(i)
		g.add_edge(pair[0], pair[1], line[m])
		count += 1
start = 0
p = Dijkstra(start, g)

print("Result of algorithm:")
for i in range(m):
	print("path to vertex %d:" % i)
	end = i
	path = []
	while end != start:
		path.append(end)
		end = p[end]
	path.append(start)
	print(path[::-1])


for i in range(m):
	print("neighbors of vertex %d:" % i)
	for j in g.adj_vertices(i):
		print(j.get_name_vertex(), sep = ' ', end = ' ')
	print('')
print("Edges of graph")	
for i in g.get_edges():
	print(i.get_name_edge(), sep = ' ', end = ' ')
print('')
print("Vertices of graph")
for i in g.get_vertices():
	print(i.get_name_vertex(), sep = ' ', end = ' ')
print('')
print(g.contains(0))
print(g.contains(10))

