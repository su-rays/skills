class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t

    def insert(self, key):
        root = self.root
        if len(root.keys) == 2 * self.t - 1:
            new_node = BTreeNode()
            new_node.children.append(self.root)
            self.split(new_node, 0)
            self.root = new_node
        self.insert_non_full(self.root, key)

    def insert_non_full(self, node, key):
        i = len(node.keys) - 1
        if node.leaf:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            node.keys.insert(i + 1, key)
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == 2 * self.t - 1:
                self.split(node, i)
                if key > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], key)

    def split(self, parent, index):
        node = parent.children[index]
        new_node = BTreeNode(node.leaf)
        mid = self.t - 1
        parent.keys.insert(index, node.keys[mid])
        parent.children.insert(index + 1, new_node)

        new_node.keys = node.keys[mid + 1:]
        node.keys = node.keys[:mid]

        if not node.leaf:
            new_node.children = node.children[mid + 1:]
            node.children = node.children[:mid + 1]

    def search(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return True
        elif node.leaf:
            return False
        else:
            return self.search(node.children[i], key)

    def display(self, node, level=0):
        print("Level", level, ":", node.keys)
        if not node.leaf:
            for child in node.children:
                self.display(child, level + 1)

if __name__ == "__main__":
    bt = BTree(t=3)

    bt.insert(10)
    bt.insert(20)
    bt.insert(5)
    bt.insert(6)
    bt.insert(30)
    bt.insert(15)

    print("Displaying BTree structure:")
    bt.display(bt.root)

    key_to_search = 15
    found = bt.search(bt.root, key_to_search)
    if found:
        print(f"Key {key_to_search} found in the BTree.")
    else:
        print(f"Key {key_to_search} not found in the BTree.")
