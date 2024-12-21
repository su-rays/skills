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