class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)
    
    def search(self, key):
        return self._search(self.root, key)
    
    def _search(self, node, key):
        if node is None:
            return None
        elif node.key == key:
            return node
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)
        
if __name__ == "__main__":
    data = [10, 20, 30, 40, 50]
    key = 60
    bst = BinarySearchTree()
    for val in data:
        bst.insert(val)
    print("all values are inserted")
    found_node = bst.search(key)
    if found_node:
        print(f"key {key} found in data {data} ")
    else:
        print(f"key {key} not found in {data}")