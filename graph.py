#!/usr/bin/env python

nodes = [
    {1: 5},
    {0: 5, 2: 2, 3: 5, 4: 1},
    {1: 2, 6: 4},
    {1: 5, 5: 1},
    {1: 1, 5: 2, 7: 3, 8: 4},
    {3: 1, 6: 2, 7: 8, 4: 2},
    {2: 4, 5: 2, 9: 3},
    {5: 8, 4: 3, 8: 1},
    {4: 4, 7: 1, 9: 1},
    {8: 1, 6: 3},
]

def dijkstra(graph, start, end):
    '''

    >>> dijkstra(nodes, 1, 7)
    (4, [1, 4, 7])
    '''
    path = [start]
    costs = [float('inf')] * len(graph)
    costs[start] = 0
    seen = set([start])

    node = start
    while node != end:
        edges = graph[node]

        smallest = end
        for i in edges.keys():
            if i in seen:
                continue

            if edges[i] < costs[i]:
                costs[i] = edges[i]
                if edges[i] <= costs[smallest]:
                    smallest = i

        node = smallest
        seen.add(node)
        path.append(node)

    print 'costs', costs, 'seen', seen

    return costs[end], path

if __name__ == '__main__':
    import doctest
    doctest.testmod()
