class Array:
    def __init__(self):
        self.arr = []

    def insert(self, value):
        self.arr.append(value)  # Insert value at the end

    def delete(self, value):
        if value in self.arr:
            self.arr.remove(value)  # Remove the first occurrence of value

    def access(self, index):
        return self.arr[index] if index < len(self.arr) else "Index out of range"

    def display(self):
        print(self.arr)

# Example Usage:
array = Array()
array.insert(10)
array.insert(20)
array.delete(10)
array.display()  # Output: [20]


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def delete(self, value):
        temp = self.head
        if temp and temp.value == value:
            self.head = temp.next  # Remove the head
            return
        while temp:
            if temp.next and temp.next.value == value:
                temp.next = temp.next.next
                return
            temp = temp.next

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")

# Example Usage:
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_list()  # Output: 1 -> 2 -> 3 -> None


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

# Example Usage:
stack = Stack()
stack.push(10)
stack.push(20)
print(stack.pop())  # Output: 20
print(stack.peek())  # Output: 10


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

# Example Usage:
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
print(queue.dequeue())  # Output: 10
print(queue.peek())  # Output: 20


class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        self.table[key] = value

    def get(self, key):
        return self.table.get(key, "Not found")

    def delete(self, key):
        if key in self.table:
            del self.table[key]
        else:
            return "Key not found"

# Example Usage:
ht = HashTable()
ht.insert("name", "Alice")
print(ht.get("name"))  # Output: Alice
ht.delete("name")
print(ht.get("name"))  # Output: Not found


#algos
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

# Example Usage:
arr = [10, 20, 30, 40, 50]
print(linear_search(arr, 30))  # Output: 2
print(linear_search(arr, 60))  # Output: -1


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example Usage:
arr = [10, 20, 30, 40, 50]
print(binary_search(arr, 30))  # Output: 2
print(binary_search(arr, 60))  # Output: -1


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example Usage:
arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))  # Output: [11, 12, 22, 25, 34, 64, 90]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example Usage:
arr = [64, 34, 25, 12, 22, 11, 90]
print(insertion_sort(arr))  # Output: [11, 12, 22, 25, 34, 64, 90]


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example Usage:
arr = [64, 34, 25, 12, 22, 11, 90]
print(selection_sort(arr))  # Output: [11, 12, 22, 25, 34, 64, 90]


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

# Example Usage:
arr = [64, 34, 25, 12, 22, 11, 90]
print(merge_sort(arr))  # Output: [11, 12, 22, 25, 34, 64, 90]


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Example Usage:
arr = [64, 34, 25, 12, 22, 11, 90]
print(quick_sort(arr))  # Output: [11, 12, 22, 25, 34, 64, 90]


import heapq

def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

# Example Usage:
arr = [64, 34, 25, 12, 22, 11, 90]
print(heap_sort(arr))  # Output: [11, 12, 22, 25, 34, 64, 90]
