class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Initial height is 1 for a single node


class AVLTree:
    # Get the height of a node
    def _height(self, node):
        if not node:
            return 0
        return node.height

    # Calculate the balance factor of a node
    def _get_balance(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    # Update height of a node based on its children's heights
    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    # Right rotation
    def _rotate_right(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        self._update_height(y)
        self._update_height(x)

        return x  # New root

    # Left rotation
    def _rotate_left(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        self._update_height(x)
        self._update_height(y)

        return y  # New root

    # Insert a key and return the new root
    def insert(self, root, key):
        # Step 1: Perform standard BST insert
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Step 2: Update the height of this ancestor node
        self._update_height(root)

        # Step 3: Get the balance factor to check if the node is unbalanced
        balance = self._get_balance(root)

        # Left Heavy (Right Rotation)
        if balance > 1 and key < root.left.key:
            return self._rotate_right(root)

        # Right Heavy (Left Rotation)
        if balance < -1 and key > root.right.key:
            return self._rotate_left(root)

        # Left-Right Heavy (Left-Right Rotation)
        if balance > 1 and key > root.left.key:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)

        # Right-Left Heavy (Right-Left Rotation)
        if balance < -1 and key < root.right.key:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)

        # Return unchanged root if balanced
        return root

    # In-order traversal for testing
    def in_order_traversal(self, root):
        if root:
            self.in_order_traversal(root.left)
            print(f"{root.key} ", end="")
            self.in_order_traversal(root.right)

# Driver Code
if __name__ == "__main__":
    avl_tree = AVLTree()
    root = None

    # Insert elements into the AVL Tree
    keys = [10, 20, 30, 40, 50, 25]
    for key in keys:
        root = avl_tree.insert(root, key)

    # Print in-order traversal of the AVL tree
    print("In-order Traversal of AVL Tree:")
    avl_tree.in_order_traversal(root)
