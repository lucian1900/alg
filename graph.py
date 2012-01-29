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
    dist = [float('inf')] * len(graph)
    dist[start] = 0
    not_seen = set(range(len(graph)))
    previous = {start: None}

    while len(not_seen) > 0 and node != end:
        # find smallest cost seen node
        node = end
        for i in not_seen:
            if graph[i] < graph[node]:
                node = i

        edges = graph[node]
        # update dist
        for i in edges.keys():
            alt = dist[node] + edges[i]
            if alt < dist[i]:
                dist[i] = alt
                previous[i] = node

        not_seen.remove(node)

    # walk back to find the path
    path = [end]
    node = end
    while node != None:
        path.append(previous[node])
        node = previous[node]

    return dist[end], path

if __name__ == '__main__':
    import doctest
    doctest.testmod()
