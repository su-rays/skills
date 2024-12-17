class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t  # Minimum degree

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


class BPlusTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []
        self.next = None

class BPlusTree:
    def __init__(self, t):
        self.root = BPlusTreeNode(True)
        self.t = t  # Minimum degree

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


import random

class Node:
    def __init__(self, value, level):
        self.value = value
        self.forward = [None] * (level + 1)

class SkipList:
    def __init__(self, max_level):
        self.max_level = max_level
        self.header = Node(None, self.max_level)
        self.level = 0

    def random_level(self):
        level = 0
        while random.random() < 0.5 and level < self.max_level:
            level += 1
        return level

    def insert(self, value):
        update = [None] * (self.max_level + 1)
        current = self.header
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current
        level = self.random_level()
        if level > self.level:
            for i in range(self.level + 1, level + 1):
                update[i] = self.header
            self.level = level
        new_node = Node(value, level)
        for i in range(level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def search(self, value):
        current = self.header
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
        current = current.forward[0]
        if current and current.value == value:
            return True
        return False

    def display(self):
        for i in range(self.level + 1):
            current = self.header.forward[i]
            print(f"Level {i}: ", end="")
            while current:
                print(current.value, end=" ")
                current = current.forward[i]
            print()


class TwoThreeTreeNode:
    def __init__(self, values=None):
        self.values = values if values else []
        self.children = []

class TwoThreeTree:
    def __init__(self):
        self.root = TwoThreeTreeNode()

    def insert(self, value):
        node, parent = self._insert(self.root, value)
        if node:
            new_root = TwoThreeTreeNode([parent.values[0]])
            new_root.children = [self.root, node]
            self.root = new_root

    def _insert(self, node, value):
        if len(node.children) == 0:
            if len(node.values) < 2:
                node.values.append(value)
                node.values.sort()
                return None, node
            else:
                node.values.append(value)
                node.values.sort()
                mid_value = node.values[1]
                new_node = TwoThreeTreeNode([node.values[2]])
                node.values = [node.values[0]]
                node.children = [node.children[0], node.children[1]]
                return new_node, mid_value
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
