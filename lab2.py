import sys

def dijkstra(graph, source, dest):
    distances = [float('inf') for i in range(len(graph))]
    visited = [False for i in range(len(graph))]
    distances[source] = 0

    if source == dest:
        return 0

    for i in range(len(graph)):
        min_dist = float('inf')
        min_index = None
        for j in range(len(graph)):
            if not visited[j] and distances[j] < min_dist:
                min_dist = distances[j]
                min_index = j
        visited[min_index] = True
        for j in range(len(graph)):
            if graph[min_index][j] and not visited[j]:
                new_dist = distances[min_index] + graph[min_index][j]
                if new_dist < distances[j]:
                    distances[j] = new_dist
    return distances[dest]

def sum_edges(graph):
    return sum([graph[i][j] for i in range(len(graph)) for j in range(i, len(graph))])

def get_unpair(graph):
    degree = [0 for i in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j]:
                degree[i] += 1
    return [i for i in range(len(degree)) if degree[i] % 2]

def gen_pairs(odds):
    pairs = []
    for i in range(len(odds) - 1):
        pairs.append([])
        for j in range(i + 1, len(odds)):
            pairs[i].append([odds[i], odds[j]])
    return pairs

def postman(graph):
    odds = get_unpair(graph)
    if not odds:
        return sum_edges(graph)
    pairs = gen_pairs(odds)
    l = (len(pairs) + 1) // 2
    pairing = []

    def get_pairs(pairs, done=[], final=[]):
        if pairs and pairs[0][0][0] not in done:
            done.append(pairs[0][0][0])
            for i in pairs[0]:
                f = final[:]
                val = done[:]
                if i[1] not in val:
                    f.append(i)
                else:
                    continue
                if len(f) == l:
                    pairing.append(f)
                    return
                else:
                    val.append(i[1])
                    get_pairs(pairs[1:], val, f)
        elif pairs:
            get_pairs(pairs[1:], done, final)

    get_pairs(pairs)
    min_sums = []
    for i in pairing:
        s = sum([dijkstra(graph, i[j][0], i[j][1]) for j in range(len(i))])
        min_sums.append(s)
    added_dis = min(min_sums)
    chinese_dis = added_dis + sum_edges(graph)
    return chinese_dis

with open('matrix_2.txt', 'r') as f:
    matrix = [[int(num) for num in line.split()] for line in f.readlines()]

print('Postman Distance is:', postman(matrix))
