class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Binary Tree Implementation
class BinaryTree:
    def __init__(self):
        self.root = None

# Binary Search Tree Implementation
class BinarySearchTree(BinaryTree):
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert(current.right, value)

# AVL Tree Implementation
class AVLTree(BinarySearchTree):
    def __init__(self):
        super().__init__()
        
    def _height(self, node):
        if node is None:
            return 0
        return max(self._height(node.left), self._height(node.right)) + 1

    def _balance_factor(self, node):
        return self._height(node.left) - self._height(node.right)

    def _rotate_left(self, z):
        y = z.right
        T = y.left
        y.left = z
        z.right = T
        return y

    def _rotate_right(self, z):
        y = z.left
        T = y.right
        y.right = z
        z.left = T
        return y

    def _balance(self, node):
        balance = self._balance_factor(node)
        if balance > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)
        return self._balance(node)

# B-Tree Implementation (Placeholder)
class BTree:
    def __init__(self, t):
        self.t = t  # Minimum degree (defines the range for number of keys)
        self.root = None

# Traversals and search algorithms
class TreeAlgorithms:
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



# Create a BST instance
bst = BinarySearchTree()

# Insert values into the BST
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(7)

# Traversals
algo = TreeAlgorithms()
print("In-Order Traversal:", algo.in_order(bst.root))  # Output: [2, 5, 7, 10, 15]
print("Pre-Order Traversal:", algo.pre_order(bst.root))  # Output: [10, 5, 2, 7, 15]
print("Post-Order Traversal:", algo.post_order(bst.root))  # Output: [2, 7, 5, 15, 10]



# Create an AVL Tree instance
avl = AVLTree()

# Insert values into the AVL Tree
avl.insert(10)
avl.insert(20)
avl.insert(5)
avl.insert(4)
avl.insert(15)

# Traversals
algo = TreeAlgorithms()
print("In-Order Traversal:", algo.in_order(avl.root))  # Balanced order: [4, 5, 10, 15, 20]
print("BFS Traversal:", algo.bfs(avl.root))  # BFS Level-Order Traversal


# Tree Traversals Example
algo = TreeAlgorithms()

# BFS and DFS Traversal
print("BFS Traversal:", algo.bfs(avl.root))  # Output: Level-wise nodes
print("DFS Traversal:", algo.dfs(avl.root))  # Output: Depth-first order


# Testing on Binary Search Tree
bst = BinarySearchTree()
for val in [30, 10, 20, 40, 50]:
    bst.insert(val)

algo = TreeAlgorithms()
print("In-Order (BST):", algo.in_order(bst.root))  # Sorted order for BST
print("BFS (BST):", algo.bfs(bst.root))

# Testing on AVL Tree
avl = AVLTree()
for val in [30, 10, 20, 40, 50]:
    avl.insert(val)

print("In-Order (AVL):", algo.in_order(avl.root))  # Balanced order
print("BFS (AVL):", algo.bfs(avl.root))  # Level-wise balanced traversal
