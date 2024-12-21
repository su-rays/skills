from collections import deque

class BfsDfs:
    @staticmethod
    def bfs_search(graph, start):
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

    @staticmethod
    def dfs_search(graph, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        result = [start]

        for neighbor in graph.get(start, []):
            if neighbor not in visited:
                result.extend(BfsDfs.dfs_search(graph, neighbor, visited))
        
        return result
    
if __name__ == "__main__":
    graph = {1: [2, 3], 2: [4], 3: [], 4: []}

    bd_fs = BfsDfs()
    print("BFS:", bd_fs.bfs_search(graph, 1))
    print("DFS:", bd_fs.dfs_search(graph, 1))