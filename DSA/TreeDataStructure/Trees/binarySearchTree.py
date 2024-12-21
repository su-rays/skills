class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def search(self, value):
        current = self.root
        while current:
            if value == current.value:
                return True  
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def find_min(self):
        current = self.root
        if current is None:
            return None
        while current.left:
            current = current.left
        return current.value

    def find_max(self):
        current = self.root
        if current is None:
            return None
        while current.right:
            current = current.right
        return current.value


if __name__ == "__main__":
    bst = BinarySearchTree()
    values = [15, 10, 20, 8, 12, 17, 25]

    for val in values:
        bst.insert(val)

    print("Search 10:", bst.search(10)) 
    print("Minimum Value:", bst.find_min())  
    print("Maximum Value:", bst.find_max())  
