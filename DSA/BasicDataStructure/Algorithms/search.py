import re

class LinearSearch:
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target

    def iterative_approach(self):
        for index in range(len(self.arr)):
            if self.arr[index] == self.target:
                return index
        return -1

    def recursive_approach(self, index=0):
        if index == len(self.arr):
            return -1
        if self.arr[index] == self.target:
            return index
        return self.recursive_approach(index + 1)
    
    def using_regex(self):
        regex = re.compile(str(self.target))
        for i, ele in enumerate(self.arr):
            if regex.search(str(ele)):
                return i
        return -1

class BinarySearch:
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target

    def iterative_approach(self):
        low, high = 0, len(self.arr) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if self.arr[mid] == self.target:
                return mid
            elif self.arr[mid] < self.target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def recursive_approach(self, low=0, high=None):
        if high is None:
            high = len(self.arr) - 1
        if high >= low:
            mid = low + (high - low) // 2
            if self.arr[mid] == self.target:
                return mid
            elif self.arr[mid] > self.target:
                return self.recursive_approach(low, mid - 1)
            else:
                return self.recursive_approach(mid + 1, high)
        return -1

if __name__ == '__main__':
    arr = [10, 23, 45, 70, 11, 15]
    target = 70

    linear_search = LinearSearch(arr, target)
    linear_result = linear_search.using_regex()
    if linear_result != -1:
        print(f"Linear Search: Element found at index {linear_result}")
    else:
        print("Linear Search: Element not found")

    sorted_arr = sorted(arr)
    binary_search = BinarySearch(sorted_arr, target)
    binary_result = binary_search.recursive_approach()
    if binary_result != -1:
        print(f"Binary Search: Element found at index {binary_result} (in sorted array)")
    else:
        print("Binary Search: Element not found")
