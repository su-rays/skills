import heapq

class Dijkstra:
    @staticmethod
    def shortest_path(graph, start, vertices):
        pq = [(0, start)]
        distances = {node: float('inf') for node in vertices}
        distances[start] = 0

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

class BellmanFord:
    @staticmethod
    def shortest_path(graph, start, vertices):
        distances = {node: float('inf') for node in vertices}
        distances[start] = 0

        for _ in range(len(vertices) - 1):
            for u in graph:
                for v, weight in graph[u]:
                    if distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight

        for u in graph:
            for v, weight in graph[u]:
                if distances[u] + weight < distances[v]:
                    raise ValueError("Graph contains a negative weight cycle")

        return distances

if __name__ == "__main__":
    graph = {
        1: [(2, 1), (3, 4)],
        2: [(3, 2)],
        3: [(4, 1)],
        4: []
    }
    vertices = [1, 2, 3, 4]

    try:
        print("Dijkstra's:", Dijkstra.shortest_path(graph, 1, vertices))
        print("Bellman-Ford:", BellmanFord.shortest_path(graph, 1, vertices))
    except ValueError as e:
        print("Error:", e)
