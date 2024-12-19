class Array:
    def __init__(self):
        self.arr = []

    def insert(self, value):
        self.arr.append(value)

    def delete(self, value):
        if value in self.arr:
            self.arr.remove(value)

    def access(self, index):
        return self.arr[index] if index < len(self.arr) else "index out of range"

    def display(self):
        print(self.arr)

array = Array()
array.insert(10)
array.insert(20)
array.insert(30)
array.delete(10)
array.display()