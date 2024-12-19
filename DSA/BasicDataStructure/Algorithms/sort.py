import heapq


class Sorting:
    def __init__(self, arr):
        self.arr = arr
        self.arrayLength = len(self.arr)
        
    def bubble_sort(self):
        for i in range(self.arrayLength):
            for j in range(0, self.arrayLength - i - 1):
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
        return self.arr

    def selection_sort(self):
        for s in range(self.arrayLength):
            min_idx = s
            for i in range(s+1, self.arrayLength):
                    if self.arr[i] < self.arr[min_idx]:
                        min_idx = i
            (self.arr[s], self.arr[min_idx]) = (self.arr[min_idx], self.arr[s])
        return self.arr

    def insertion_sort(self):
        for i in range(1, self.arrayLength):
            a = self.arr[i]
            j = i - 1
            while j >= 0 and a < self.arr[j]:
                    self.arr[j+1] = self.arr[j]
                    j -= 1
            self.arr[j+1] = a
        return self.arr

    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            self.merge_sort(left)
            self.merge_sort(right)

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
        
    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quick_sort(left) + middle + self.quick_sort(right)
    
    def heap_sort(self):
        heapq.heapify(self.arr)
        return [heapq.heappop(self.arr) for _ in range(self.arrayLength)]
                    
if __name__ == '__main__':
    arr = [2, 1, 10, 23]
    cls_obj = Sorting(arr)
    sorted_arr = cls_obj.merge_sort(arr)
    print(f"Sorted array: {sorted_arr}")