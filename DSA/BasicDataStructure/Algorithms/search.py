import re
from .argument_parser import arg_parser

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
        self.low = 0
        self.high = len(self.arr) - 1

    def iterative_approach(self):
        while self.low <= self.high:
            mid = self.low + (self.high - self.low) // 2
            if self.arr[mid] == self.target:
                return mid
            elif self.arr[mid] < self.target:
                self.low = mid + 1
            else:
                self.high = mid - 1
        return -1

    def recursive_approach_helper(self, low, high):
        if high >= low:
            mid = low + (high - low) // 2
            if self.arr[mid] == self.target:
                return mid
            elif self.arr[mid] > self.target:
                return self.recursive_approach_helper(low, mid - 1)
            else:
                return self.recursive_approach_helper(mid + 1, high)
        return -1

    def recursive_approach(self):
        return self.recursive_approach_helper(self.low, self.high)

if __name__ == '__main__':
    args = arg_parser()
    
    arr = list(map(int, args.arr.split(',')))
    target = args.target

    if args.algorithm == "binary":
        arr.sort()
        cls_obj = BinarySearch(arr, target)
        if args.approach == "iterative":
            result = cls_obj.iterative_approach()
        elif args.approach == "recursive":
            result = cls_obj.recursive_approach()
        else:
            print("Regex approach is not supported for binary search")
            exit(1)

    else:
        cls_obj = LinearSearch(arr, target)
        if args.approach == "iterative":
            result = cls_obj.iterative_approach()
        elif args.approach == "recursive":
            result = cls_obj.recursive_approach()
        elif args.approach == "regex":
            result = cls_obj.using_regex()

    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the array")
