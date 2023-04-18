def read_graph(filename):
    with open(filename) as f:
        return [[int(num) for num in line.split()] for line in f]

graph1 = read_graph('graph1.txt')
graph2 = read_graph('graph2.txt')

if graph1 != graph2 and list(map(len, graph1)) != list(map(len, graph2)):
    print("Not isomorphic")
else:
    print("Isomorphic")