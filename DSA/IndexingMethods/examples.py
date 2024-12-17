class LinearIndexing:
    def __init__(self, data):
        self.data = data

    def search(self, key):
        for index, value in enumerate(self.data):
            if value == key:
                return index
        return -1

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
        if node.key == key:
            return node
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)
        
if __name__ == '__main__':
    ''' Linear Indexing '''
    key = 30
    data = [10, 20, 30, 40, 50]
    indexer = LinearIndexing(data)

    ''' Tree Based Indexing '''
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(20)
    bst.insert(30)
    bst.insert(40)
    bst.insert(50)

    index = indexer.search(key)
    found_node = bst.search(key)

    if index != -1 or found_node:
        print(f"Key {key} found")
    else:
        print(f"Key {key} not found.")

