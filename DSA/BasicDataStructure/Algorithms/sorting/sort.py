class Sorting:
    def __init__(self, arr):
        self.arr = arr
        self.arrayLength = len(self.arr)
        
    def bubble_sort(self):
        for i in range(self.arrayLength):
            for j in range(0, self.arrayLength - i - 1):
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]

    def selection_sort(self):
        for s in range(self.arrayLength):
            min_idx = s
            for i in range(s+1, self.arrayLength):
                    if self.arr[i] < self.arr[min_idx]:
                        min_idx = i
            (self.arr[s], self.arr[min_idx]) = (self.arr[min_idx], self.arr[s])

    def insertion_sort(self):
        for i in range(1, self.arrayLength):
            a = self.arr[i]
            j = i - 1
            while j >= 0 and a < self.arr[j]:
                    self.arr[j+1] = self.arr[j]
                    j -= 1
            self.arr[j+1] = a
        

                    
if __name__ == '__main__':
    arr = [2, 1, 10, 23]
    cls_obj = Sorting(arr)
    cls_obj.bubble_sort()
    print(f"Sorted array is: ")
    for i in range(len(cls_obj.arr)):
        print("%d" % cls_obj.arr[i])
