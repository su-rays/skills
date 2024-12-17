1. Directed Graph Class
python
Copy code
class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        """Adds a directed edge from node u to node v."""
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def __str__(self):
        """Returns the string representation of the graph."""
        return str(self.graph)
2. Undirected Graph Class
python
Copy code
class UndirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        """Adds an undirected edge between nodes u and v."""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def __str__(self):
        """Returns the string representation of the graph."""
        return str(self.graph)
3. Breadth First Search (BFS)
python
Copy code
from collections import deque

class BFS:
    @staticmethod
    def search(graph, start):
        """Performs BFS starting from node `start`."""
        visited = set()
        queue = deque([start])
        visited.add(start)
        result = []

        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
4. Depth First Search (DFS)
python
Copy code
class DFS:
    @staticmethod
    def search(graph, start, visited=None):
        """Performs DFS starting from node `start`."""
        if visited is None:
            visited = set()
        visited.add(start)
        result = [start]

        for neighbor in graph.get(start, []):
            if neighbor not in visited:
                result.extend(DFS.search(graph, neighbor, visited))
        
        return result
5. Dijkstra's Algorithm (Shortest Path)
python
Copy code
import heapq

class Dijkstra:
    @staticmethod
    def shortest_path(graph, start):
        """Finds the shortest path from start node to all other nodes."""
        pq = [(0, start)]  # Priority queue with (distance, node)
        distances = {start: 0}
        
        while pq:
            current_distance, current_node = heapq.heappop(pq)
            
            if current_distance > distances.get(current_node, float('inf')):
                continue
            
            for neighbor, weight in graph.get(current_node, []):
                distance = current_distance + weight
                if distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances
6. Bellman-Ford Algorithm (Shortest Path with Negative Edges)
python
Copy code
class BellmanFord:
    @staticmethod
    def shortest_path(graph, start, vertices):
        """Finds the shortest path from start node to all other nodes, handles negative edges."""
        distances = {node: float('inf') for node in vertices}
        distances[start] = 0

        for _ in range(len(vertices) - 1):
            for u in graph:
                for v, weight in graph[u]:
                    if distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight

        # Check for negative weight cycles
        for u in graph:
            for v, weight in graph[u]:
                if distances[u] + weight < distances[v]:
                    raise ValueError("Graph contains negative weight cycle")

        return distances
7. Prim's Algorithm (Minimum Spanning Tree)
python
Copy code
import heapq

class Prim:
    @staticmethod
    def minimum_spanning_tree(graph):
        """Finds the minimum spanning tree using Prim's Algorithm."""
        start = next(iter(graph))  # Start from any node
        mst = []
        visited = set([start])
        edges = [(weight, start, neighbor) for neighbor, weight in graph[start]]
        heapq.heapify(edges)

        while edges:
            weight, u, v = heapq.heappop(edges)
            if v not in visited:
                visited.add(v)
                mst.append((u, v, weight))
                for neighbor, w in graph[v]:
                    if neighbor not in visited:
                        heapq.heappush(edges, (w, v, neighbor))

        return mst
8. Kruskal's Algorithm (Minimum Spanning Tree)
python
Copy code
class UnionFind:
    def __init__(self, vertices):
        """Initializes the Union-Find data structure."""
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, u):
        """Finds the root of the set containing u."""
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        """Unites the sets containing u and v."""
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

class Kruskal:
    @staticmethod
    def minimum_spanning_tree(graph, vertices):
        """Finds the minimum spanning tree using Kruskal's Algorithm."""
        edges = []
        for u in graph:
            for v, weight in graph[u]:
                edges.append((weight, u, v))
        edges.sort()  # Sort by weight

        uf = UnionFind(vertices)
        mst = []

        for weight, u, v in edges:
            if uf.union(u, v):
                mst.append((u, v, weight))

        return mst
Example Usage:
python
Copy code
# Directed Graph
dg = DirectedGraph()
dg.add_edge(1, 2)
dg.add_edge(1, 3)
dg.add_edge(2, 4)
print("Directed Graph:", dg)

# Undirected Graph
ug = UndirectedGraph()
ug.add_edge(1, 2)
ug.add_edge(2, 3)
ug.add_edge(1, 3)
print("Undirected Graph:", ug)

# BFS
graph_bfs = {1: [2, 3], 2: [4], 3: [], 4: []}
print("BFS:", BFS.search(graph_bfs, 1))

# DFS
graph_dfs = {1: [2, 3], 2: [4], 3: [], 4: []}
print("DFS:", DFS.search(graph_dfs, 1))

# Dijkstra's
graph_dijkstra = {1: [(2, 1), (3, 4)], 2: [(3, 2)], 3: [(4, 1)], 4: []}
print("Dijkstra's:", Dijkstra.shortest_path(graph_dijkstra, 1))

# Bellman-Ford
graph_bf = {1: [(2, 1), (3, 4)], 2: [(3, -2)], 3: [(4, 1)], 4: []}
vertices_bf = [1, 2, 3, 4]
print("Bellman-Ford:", BellmanFord.shortest_path(graph_bf, 1, vertices_bf))

# Prim's MST
graph_prim = {1: [(2, 1), (3, 4)], 2: [(3, 2)], 3: [(4, 1)], 4: []}
print("Prim's MST:", Prim.minimum_spanning_tree(graph_prim))

# Kruskal's MST
graph_kruskal = {1: [(2, 1), (3, 4)], 2: [(3, 2)], 3: [(4, 1)], 4: []}
vertices_kruskal = [1, 2, 3, 4]
print("Kruskal's MST:", Kruskal.minimum_spanning_tree(graph_kruskal, v