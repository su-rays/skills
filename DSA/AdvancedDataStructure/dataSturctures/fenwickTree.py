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


fenwick = FenwickTree(6)
fenwick.update(1, 5)
fenwick.update(2, 3)
fenwick.update(3, 2)
print(fenwick.query(3))