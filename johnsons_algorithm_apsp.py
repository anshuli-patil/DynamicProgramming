import sys
import copy
from collections import defaultdict


def johnson(G):
    G.add_node(-1)

    for v in G.nodes:
        G.add_edge(-1, v, 0)

    result = bellman_ford(G, -1)

    if result is None:
        print ('Negative cycle detected')
        return

    for u in G.nodes:
        for v in G.edges[u]:
            G.distances[(u, v)] = G.distances[(u, v)] + result[u] - result[v]
    G.nodes.remove(-1)
    del G.edges[-1]

    paths = {}
    for u in G.nodes:
        visited = dijsktra(G, u)[0]
        for v in visited:
            paths[(u, v)] = visited[v]

    '''
    for edge in G.edges:
        u = edge
        for v in G.edges :
            if u != v and (u, v) in paths and u != -1 and v != -1:
                paths[(u, v)] = paths[(u, v)] - result[(-1, u)] + result[(-1, v)]
    '''
    return paths, result


def get_real_shortest_path(paths, result, u, v):
    if (u, v) in paths:
        return paths[(u, v)] - result[u] + result[v]
    else:
        return float('inf')


def bellman_ford(g, source):
    paths = defaultdict(lambda: float('inf'))
    paths[source] = 0
    for i in range(1, len(g.nodes)):
        for u in g.nodes:
            for v in g.edges[u]:
                paths[v] = min(paths[v], paths[u] + g.distances[(u, v)])

    for u in g.nodes:
        for v in g.edges[u]:
            if paths[v] > (paths[u] + g.distances[(u, v)]):
                # Negative edges in graph g
                return None

    return paths


def dijsktra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node
    # print(initial, visited)
    return visited, path


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = defaultdict(lambda: float('inf'))

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance


G = Graph()
line1 = (input().strip()).split(' ')
t = int(line1[1])
n = int(line1[0])

for a0 in range(t):
    line = (input().strip()).split(' ')
    m = int(line[0])
    n = int(line[1])
    a = int(line[2])
    G.add_node(m)
    G.add_node(n)
    G.add_edge(m, n, a)

print(n, t)
q = int(input().strip())
print('started')

'''
min_val = float('inf')
for i in range(1, n + 1):
    distances_bellman = bellman_ford(G, i)
    min_val = min(distances_bellman)
    print('current min '+str(min_val))
print(min_val)
print(q)
'''

paths, result = johnson(G)
min_val = float('inf')

for i in range(q):
    line = (input().strip()).split(' ')
    m = int(line[0])
    n = int(line[1])
    dist_q = get_real_shortest_path(paths, result, m, n)
    if dist_q == float('inf'):
        print(-1)
    else:
        print (dist_q)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        min_val = min(min_val, get_real_shortest_path(paths, result, i, j))
print(min_val)



'''
G = Graph()
for i in range(1, 6):
    G.add_node(i)
G.add_edge(1, 2, -1)
G.add_edge(1, 3, 4)
G.add_edge(2, 3, 3)
G.add_edge(2, 4, 2)
G.add_edge(2, 5, 2)
G.add_edge(3, 2, 4)
G.add_edge(3, 1, 6)
G.add_edge(4, 2, 1)
G.add_edge(4, 3, 5)
G.add_edge(5, 4, -3)
G.add_edge(5, 2, 1)
# print(bellman_ford(G, 1))

paths_answers = {}
paths, result = (johnson(copy.deepcopy(G)))
for i in range(1, 6):
    for j in range(1, 6):
        paths_answers[(i, j)] = (get_real_shortest_path(paths, result, i, j))
for i in range(1, 6):
    distances_bellman = bellman_ford(G, i)
    for j in range(1, 6):
        if distances_bellman[j] != paths_answers[(i, j)]:
            print(i, j, distances_bellman[j], paths_answers[(i, j)])

'''
