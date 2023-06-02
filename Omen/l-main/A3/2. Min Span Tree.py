import sys

def prim(graph):
    start_vertex = list(graph.keys())[0]
    visited = set()
    mst = []
    min_weights = {vertex: sys.maxsize for vertex in graph}
    min_weights[start_vertex] = 0

    while len(visited) != len(graph):
        min_weight = sys.maxsize
        min_vertex = None
        for vertex in graph:
            if vertex not in visited and min_weights[vertex] < min_weight:
                min_weight = min_weights[vertex]
                min_vertex = vertex

        visited.add(min_vertex)

        if min_vertex is not None:
            mst.append((min_vertex, min_weights[min_vertex]))

        for neighbor, weight in graph[min_vertex].items():
            if neighbor not in visited and weight < min_weights[neighbor]:
                min_weights[neighbor] = weight

    return mst

# Example graph
graph = {
    'A': {'B': 2, 'D': 1},
    'B': {'A': 2, 'C': 3, 'D': 2},
    'C': {'B': 3, 'D': 4},
    'D': {'A': 1, 'B': 2, 'C': 4}
}

mst = prim(graph)

print("Minimum Spanning Tree:")
for vertex, weight in mst:
    print(f"Edge: {vertex} - {weight}")
