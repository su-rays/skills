class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    traversal = Traversal()

    print("Pre-order Traversal:", traversal.pre_order(root))  
    print("In-order Traversal:", traversal.in_order(root))  
    print("Post-order Traversal:", traversal.post_order(root))