import heapq

class Prim:
    @staticmethod
    def minimum_spanning_tree(graph):
        start = next(iter(graph))
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

class KruskalUnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

    @staticmethod
    def minimum_spanning_tree(graph, vertices):
        edges = []
        for u in graph:
            for v, weight in graph[u]:
                edges.append((weight, u, v))
        edges.sort()
        kruskal_union_find = KruskalUnionFind(vertices)
        mst = []

        for weight, u, v in edges:
            if kruskal_union_find.union(u, v):
                mst.append((u, v, weight))

        return mst

if __name__ == "__main__":
    graph = {1: [(2, 1), (3, 4)], 2: [(3, 2)], 3: [(4, 1)], 4: []}
    vertices_kruskal = [1, 2, 3, 4]

    print("Prim's MST:", Prim.minimum_spanning_tree(graph))
    print("Kruskal's MST:", KruskalUnionFind.minimum_spanning_tree(graph, vertices_kruskal))