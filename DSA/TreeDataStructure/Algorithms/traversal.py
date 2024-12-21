class Traversal:
    def pre_order(self, root):
        if root is None:
            return []
        return [root.value] + self.pre_order(root.left) + self.pre_order(root.right)

    def in_order(self, root):
        if root is None:
            return []
        return self.in_order(root.left) + [root.value] + self.in_order(root.right)

    def post_order(self, root):
        if root is None:
            return []
        return self.post_order(root.left) + self.post_order(root.right) + [root.value]
