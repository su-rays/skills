# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# # Binary Tree Implementation
# class BinaryTree:
#     def __init__(self):
#         self.root = None

# # Binary Search Tree Implementation
# class BinarySearchTree(BinaryTree):
#     def insert(self, value):
#         if self.root is None:
#             self.root = Node(value)
#         else:
#             self._insert(self.root, value)

#     def _insert(self, current, value):
#         if value < current.value:
#             if current.left is None:
#                 current.left = Node(value)
#             else:
#                 self._insert(current.left, value)
#         else:
#             if current.right is None:
#                 current.right = Node(value)
#             else:
#                 self._insert(current.right, value)

class Node:
    def __init__(self, value):
        """Initialize a node with a value and no children."""
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        """Initialize the root of the tree."""
        self.root = None

    def insert(self, value):
        """Insert a value into the BST."""
        new_node = Node(value)
        if self.root is None:  # If the tree is empty, set the root
            self.root = new_node
            return
        
        current = self.root
        while True:
            if value < current.value:  # Go to the left subtree
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:  # Go to the right subtree
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def search(self, value):
        """Search for a value in the BST. Returns True if found, False otherwise."""
        current = self.root
        while current:
            if value == current.value:
                return True  # Value found
            elif value < current.value:
                current = current.left  # Search left subtree
            else:
                current = current.right  # Search right subtree
        return False  # Value not found

    def find_min(self):
        """Find the minimum value in the BST."""
        current = self.root
        if current is None:
            return None  # Tree is empty
        while current.left:
            current = current.left
        return current.value

    def find_max(self):
        """Find the maximum value in the BST."""
        current = self.root
        if current is None:
            return None  # Tree is empty
        while current.right:
            current = current.right
        return current.value

    def inorder_traversal(self, node):
        """Inorder traversal of the BST (Left, Root, Right)."""
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=' ')
            self.inorder_traversal(node.right)

# Example usage
if __name__ == "__main__":
    bst = BinarySearchTree()
    values = [15, 10, 20, 8, 12, 17, 25]

    # Insert values into the BST
    for val in values:
        bst.insert(val)
    
    print("Inorder Traversal (Sorted Order):")
    bst.inorder_traversal(bst.root)  # Output: 8 10 12 15 17 20 25

    # Search for values
    print("\nSearch 10:", bst.search(10))  # True
    print("Search 99:", bst.search(99))  # False

    # Find min and max values
    print("Minimum Value:", bst.find_min())  # 8
    print("Maximum Value:", bst.find_max())  # 25
