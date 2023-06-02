import sys

def dijkstra(graph, source):
    # Initialize distances with infinity except for the source vertex
    distances = {vertex: sys.maxsize for vertex in graph}
    distances[source] = 0

    # Initialize an empty set to store visited vertices
    visited = set()

    while len(visited) != len(graph):
        # Find the vertex with the minimum distance
        min_distance = sys.maxsize
        min_vertex = None
        for vertex in graph:
            if vertex not in visited and distances[vertex] < min_distance:
                min_distance = distances[vertex]
                min_vertex = vertex

        # Add the minimum distance vertex to the visited set
        visited.add(min_vertex)

        # Update distances of adjacent vertices
        for neighbor, weight in graph[min_vertex].items():
            if distances[min_vertex] + weight < distances[neighbor]:
                distances[neighbor] = distances[min_vertex] + weight

    return distances


# Example graph
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'C': 1, 'D': 5},
    'C': {'D': 1},
    'D': {'A': 3}
}

# Set the source vertex
source_vertex = 'A'

# Find the shortest paths from the source vertex using Dijkstra's algorithm
shortest_paths = dijkstra(graph, source_vertex)

# Print the shortest paths
for vertex, distance in shortest_paths.items():
    print(f"Shortest path from {source_vertex} to {vertex} is {distance}")
