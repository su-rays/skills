class TwoThreeTreeNode:
    def __init__(self, values=None):
        self.values = values if values else []
        self.children = []

class TwoThreeTree:
    def __init__(self):
        self.root = TwoThreeTreeNode()

    def insert(self, value):
        node, parent, is_new_root = self._insert(self.root, value)
        
        if is_new_root:
            new_root = TwoThreeTreeNode([parent])
            new_root.children = [self.root, node]
            self.root = new_root

    def _insert(self, node, value):
        if len(node.children) == 0:
            if len(node.values) < 2:
                node.values.append(value)
                node.values.sort()
                return None, None, False
            else:
                node.values.append(value)
                node.values.sort()
                mid_value = node.values[1]
                new_node = TwoThreeTreeNode([node.values[2]])
                node.values = [node.values[0]]
                node.children = []
                return new_node, mid_value, True
        else:
            if value < node.values[0]:
                return self._insert(node.children[0], value)
            elif len(node.values) == 1 or value < node.values[1]:
                return self._insert(node.children[1], value)
            else:
                return self._insert(node.children[2], value)

    def search(self, node, value):
        if node is None:
            return False
        if value in node.values:
            return True
        elif len(node.children) == 0:
            return False
        elif value < node.values[0]:
            return self.search(node.children[0], value)
        elif len(node.values) == 1 or value < node.values[1]:
            return self.search(node.children[1], value)
        else:
            return self.search(node.children[2], value)

    def display(self, node, level=0):
        print("Level", level, ":", node.values)
        for child in node.children:
            self.display(child, level + 1)


    def search(self, node, value):
        if node is None:
            return False
        if value in node.values:
            return True
        elif len(node.children) == 0:
            return False
        elif value < node.values[0]:
            return self.search(node.children[0], value)
        elif len(node.values) == 1 or value < node.values[1]:
            return self.search(node.children[1], value)
        else:
            return self.search(node.children[2], value)

    def display(self, node, level=0):
        print("Level", level, ":", node.values)
        for child in node.children:
            self.display(child, level + 1)

if __name__ == "__main__":
    tree = TwoThreeTree()

    values_to_insert = [10, 20, 5, 6, 15, 30, 25]
    for value in values_to_insert:
        tree.insert(value)

    print("Displaying TwoThreeTree structure:")
    tree.display(tree.root)

    search_values = [15, 6, 25, 40]
    for value in search_values:
        found = tree.search(tree.root, value)
        if found:
            print(f"Value {value} found in the TwoThreeTree.")
        else:
            print(f"Value {value} not found in the TwoThreeTree.")
