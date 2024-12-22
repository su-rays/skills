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

    def print_tree(self):
        if not self.root:
            print("Tree is empty")
            return
        
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            print(current.value, end=" ")

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        print()

values = [1, 2, 3, 4, 5, 6, 7]
bt = BinaryTree()
bt.insert_level_order(values)
bt.print_tree()
