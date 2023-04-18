def postman(graph):
    odds = get_unpair(graph)
    if not odds:
        return sum_edges(graph)
    pairs = gen_pairs(odds)
    pairing = []

    def get_pairs(pairs, done=[], final=[]):
        if pairs and pairs[0][0][0] not in done:
            done.append(pairs[0][0][0])
            for i in pairs[0]:
                if i[1] not in done:
                    f = final + [i] if len(final) < len(pairs) // 2 else final
                    val = done + [i[1]]
                    if len(f) == len(pairs) // 2:
                        pairing.append(f)
                        return
                    else:
                        get_pairs(pairs[1:], val, f)
        elif pairs:
            get_pairs(pairs[1:], done, final)

    get_pairs(pairs)
    min_sums = [sum(dijkstra(graph, i[j][0], i[j][1]) for j in range(len(i))) for i in pairing]
    return min(min_sums) + sum_edges(graph)