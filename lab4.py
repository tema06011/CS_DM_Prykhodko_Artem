class Graph:
    def __init__(self, graph):
        self.graph = graph

    def BFS(self, s, t, parent):
        visited = set()
        queue = [s]
        visited.add(s)
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if ind not in visited and val > 0:
                    queue.append(ind)
                    visited.add(ind)
                    parent[ind] = u
                    if ind == t:
                        return True
        return False

    def FordFulkerson(self, source, sink):
        parent = [-1] * len(self.graph)
        max_flow = 0
        while True:
            if not self.BFS(source, sink, parent):
                break
            path_flow = float("inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_flow

with open('graph.txt', 'r') as f:
    graph = [[int(num) for num in line.split()] for line in f]

g = Graph(graph)
source = 0
sink = len(graph) - 1
print("The maximum possible flow is %d " % g.FordFulkerson(source, sink))