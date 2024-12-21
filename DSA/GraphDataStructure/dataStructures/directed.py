class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def __str__(self):
        return str(self.graph)
    
if __name__ == "__main__":
    dg = DirectedGraph()
    dg.add_edge(1, 2)
    dg.add_edge(1, 3)
    dg.add_edge(2, 4)
    print("Directed Graph:", dg)