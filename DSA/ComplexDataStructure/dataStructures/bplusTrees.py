class BPlusTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []
        self.next = None

class BPlusTree:
    def __init__(self, t):
        self.root = BPlusTreeNode(True)
        self.t = t

    def insert(self, key):
        root = self.root
        if len(root.keys) == 2 * self.t - 1:
            new_node = BPlusTreeNode()
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
        new_node = BPlusTreeNode(node.leaf)
        mid = self.t - 1
        parent.keys.insert(index, node.keys[mid])
        parent.children.insert(index + 1, new_node)

        new_node.keys = node.keys[mid + 1:]
        node.keys = node.keys[:mid]

        if node.leaf:
            new_node.next = node.next
            node.next = new_node
        else:
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

    def display(self, node):
        if node.leaf:
            print(node.keys)
        else:
            for child in node.children:
                self.display(child)

if __name__ == "__main__":
    bpt = BPlusTree(t=3)

    bpt.insert(10)
    bpt.insert(20)
    bpt.insert(5)
    bpt.insert(6)
    bpt.insert(30)
    bpt.insert(15)

    print("Displaying BPlusTree structure:")
    bpt.display(bpt.root)

    key_to_search = 15
    found = bpt.search(bpt.root, key_to_search)
    if found:
        print(f"Key {key_to_search} found in the BPlusTree.")
    else:
        print(f"Key {key_to_search} not found in the BPlusTree.")
