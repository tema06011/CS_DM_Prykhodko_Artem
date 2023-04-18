class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self):
        result = []
        i = 0
        e = 0

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        return result

# read the matrix from file
filename = "matrix.txt"
with open(filename) as f:
    matrix = [list(map(int, line.split())) for line in f.readlines()]

# determine the number of vertices
V = len(matrix)

# create the graph and add edges
g = Graph(V)
for i in range(V):
    for j in range(i+1, V):
        if matrix[i][j] != 0:
            g.add_edge(i, j, matrix[i][j])

# find the minimum spanning tree
mst = g.kruskal_mst()

# print the results
print("MST edges:")
for u, v, weight in mst:
    print(f"{u} -- {v} : {weight}")
