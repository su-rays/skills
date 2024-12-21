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

if __name__ == "__main__":
    skip_list = SkipList(max_level=4)

    skip_list.insert(3)
    skip_list.insert(6)
    skip_list.insert(7)
    skip_list.insert(9)
    skip_list.insert(12)
    skip_list.insert(19)
    skip_list.insert(17)
    skip_list.insert(26)

    print("Displaying SkipList structure:")
    skip_list.display()

    search_values = [6, 15, 19, 10]
    for value in search_values:
        found = skip_list.search(value)
        if found:
            print(f"Value {value} found in the SkipList.")
        else:
            print(f"Value {value} not found in the SkipList.")
