class UndirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def __str__(self):
        return str(self.graph)
    
if __name__ == "__main__":
    ug = UndirectedGraph()
    ug.add_edge(1, 2)
    ug.add_edge(2, 3)
    ug.add_edge(1, 3)
    print("Undirected Graph:", ug)