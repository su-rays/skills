class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Example usage
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))  # True
print(trie.search("app"))    # False
print(trie.starts_with("app"))  # True


class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        self.build(arr)
    
    def build(self, arr):
        # Insert leaf nodes in the tree
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        # Build the segment tree by calculating parents
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
    
    def update(self, idx, value):
        idx += self.n
        self.tree[idx] = value
        while idx > 1:
            idx //= 2
            self.tree[idx] = self.tree[2 * idx] + self.tree[2 * idx + 1]
    
    def query(self, left, right):
        left += self.n
        right += self.n
        sum_ = 0
        while left <= right:
            if left % 2 == 1:
                sum_ += self.tree[left]
                left += 1
            if right % 2 == 0:
                sum_ += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return sum_

# Example usage
arr = [1, 3, 5, 7, 9, 11]
seg_tree = SegmentTree(arr)
print(seg_tree.query(1, 3))  # Sum of elements from index 1 to 3
seg_tree.update(2, 6)
print(seg_tree.query(1, 3))  # Updated sum


class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def update(self, idx, delta):
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & -idx
    
    def query(self, idx):
        sum_ = 0
        while idx > 0:
            sum_ += self.tree[idx]
            idx -= idx & -idx
        return sum_

# Example usage
fenwick = FenwickTree(6)
fenwick.update(1, 5)
fenwick.update(2, 3)
fenwick.update(3, 2)
print(fenwick.query(3))  # Sum of elements from index 1 to 3


class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

# Example usage
ds = DisjointSet(5)
ds.union(0, 1)
ds.union(2, 3)
print(ds.find(0))  # Should print 1
print(ds.find(2))  # Should print 3
ds.union(1, 3)
print(ds.find(0))  # Should print 3, as 0 is connected to 3


class SuffixArray:
    def __init__(self, text):
        self.text = text
        self.suffix_array = self.build_suffix_array(text)
    
    def build_suffix_array(self, text):
        suffixes = [(text[i:], i) for i in range(len(text))]
        suffixes.sort()  # Sort suffixes lexicographically
        return [suffix[1] for suffix in suffixes]
    
    def display(self):
        return self.suffix_array

# Example usage
text = "banana"
suffix_arr = SuffixArray(text)
print(suffix_arr.display())  # Indices of suffixes in sorted order
