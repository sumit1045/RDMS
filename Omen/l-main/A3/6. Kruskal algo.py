class DisjointSet:
    def _init_(self, vertices):
        self.parent = {}
        for vertex in vertices:
            self.parent[vertex] = vertex
        self.rank = dict.fromkeys(vertices, 0)

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

def kruskal(graph):
    vertices = list(graph.keys())
    edges = []

    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            edges.append((vertex, neighbor, weight))

    edges.sort(key=lambda x: x[2])  # Sort edges by weight

    mst = []
    disjoint_set = DisjointSet(vertices)

    for edge in edges:
        vertex1, vertex2, weight = edge
        root1 = disjoint_set.find(vertex1)
        root2 = disjoint_set.find(vertex2)
        if root1 != root2:
            mst.append((vertex1, vertex2, weight))
            disjoint_set.union(root1, root2)

    return mst

# Example graph
graph = {
    'A': {'B': 2, 'D': 1},
    'B': {'A': 2, 'C': 3, 'D': 2},
    'C': {'B': 3, 'D': 4},
    'D': {'A': 1, 'B': 2, 'C': 4}
}

mst = kruskal(graph)

print("Minimal Spanning Tree:")
for vertex1, vertex2, weight in mst:
    print(f"Edge: {vertex1} - {vertex2}, Weight: {weight}")
