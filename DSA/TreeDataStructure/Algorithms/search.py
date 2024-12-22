class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Searching:
    def bfs(self, root):
        if root is None:
            return []
        queue = [root]
        result = []
        while queue:
            current = queue.pop(0)
            result.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result

    def dfs(self, root):
        if root is None:
            return []
        stack = [root]
        result = []
        while stack:
            current = stack.pop()
            result.append(current.value)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return result

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    search = Searching()

    bfs_result = search.bfs(root)
    dfs_result = search.dfs(root)

    print("BFS Result:", bfs_result)
    print("DFS Result:", dfs_result)
