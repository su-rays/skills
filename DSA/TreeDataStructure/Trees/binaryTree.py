class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_level_order(self, values):
        if not values:
            return None
        
        self.root = Node(values[0])
        queue = [self.root]
        i = 1

        while i < len(values):
            current = queue.pop(0)
            
            if i < len(values):
                current.left = Node(values[i])
                queue.append(current.left)
                i += 1
            
            if i < len(values):
                current.right = Node(values[i])
                queue.append(current.right)
                i += 1

    def inorder_traversal(self, node):
        if node is None:
            return []
        return (self.inorder_traversal(node.left) +
                [node.value] +
                self.inorder_traversal(node.right))

    def preorder_traversal(self, node):
        if node is None:
            return []
        return ([node.value] +
                self.preorder_traversal(node.left) +
                self.preorder_traversal(node.right))

    def postorder_traversal(self, node):
        if node is None:
            return []
        return (self.postorder_traversal(node.left) +
                self.postorder_traversal(node.right) +
                [node.value])

# Example usage:
values = [1, 2, 3, 4, 5, 6, 7]  # Complete binary tree
bt = BinaryTree()
bt.insert_level_order(values)

print("Inorder Traversal:", bt.inorder_traversal(bt.root))
print("Preorder Traversal:", bt.preorder_traversal(bt.root))
print("Postorder Traversal:", bt.postorder_traversal(bt.root))
