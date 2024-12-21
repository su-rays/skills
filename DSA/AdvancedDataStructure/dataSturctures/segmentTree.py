class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        self.build(arr)
    
    def build(self, arr):
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
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

arr = [1, 3, 5, 7, 9, 11]
seg_tree = SegmentTree(arr)
print(seg_tree.query(1, 3))
seg_tree.update(2, 6)
print(seg_tree.query(1, 3))