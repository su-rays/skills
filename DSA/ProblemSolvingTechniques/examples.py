import random

class ProblemSolvingTechniques:
    def brute_force_pairs(arr, target):
        '''Brute-Force algorithm: Finds pairs in an array whose sum equals the target.'''
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] + arr[j] == target:
                    print(arr[i], arr[j])

    def greedy_activity_selection(start, finish):
        '''Greedy algorithm: Selects the maximum number of activities that don't overlap.'''
        activities = list(zip(start, finish))
        activities.sort(key=lambda x: x[1])
        
        selected = []
        last_finish_time = 0
        
        for s, f in activities:
            if s >= last_finish_time:
                selected.append((s, f))
                last_finish_time = f
        
        print("Selected activities:", selected)

    def merge_sort(arr):
        '''Divide and Conquer algorithm: Implements Merge Sort.'''
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            ProblemSolvingTechniques.merge_sort(left)
            ProblemSolvingTechniques.merge_sort(right)

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

    def fib(n):
        '''Dynamic Programming: Calculates the nth Fibonacci number.'''
        if n <= 1:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
    
    def is_safe(board, row, col, n):
        '''Helper function for the N-Queens problem: Checks if a position is safe.'''
        for i in range(col):
            if board[row][i] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        return True

    def solve_n_queens(board, col, n):
        '''Recursive helper function for the N-Queens problem.'''
        if col >= n:
            for row in board:
                print(row)
            return True

        res = False
        for i in range(n):
            if ProblemSolvingTechniques.is_safe(board, i, col, n):
                board[i][col] = 1
                res = ProblemSolvingTechniques.solve_n_queens(board, col + 1, n) or res
                board[i][col] = 0
        return res
    
    def n_queens(n):
        '''Backtracking: Solves the N-Queens problem.'''
        board = [[0 for _ in range(n)] for _ in range(n)]
        ProblemSolvingTechniques.solve_n_queens(board, 0, n)

    def partition(arr, low, high):
        '''Helper function for Quick Sort: Partitions the array around a pivot.'''
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def randomized_quick_sort(arr, low, high):
        '''Randomized Algorithm: Implements Randomized Quick Sort.'''
        if low < high:
            pivot = random.randint(low, high)
            arr[pivot], arr[high] = arr[high], arr[pivot]
            pi = ProblemSolvingTechniques.partition(arr, low, high)
            ProblemSolvingTechniques.randomized_quick_sort(arr, low, pi - 1)
            ProblemSolvingTechniques.randomized_quick_sort(arr, pi + 1, high)

    def factorial(n):
        '''Recursion: Calculates the factorial of a number.'''
        if n == 0:
            return 1
        else:
            return n * ProblemSolvingTechniques.factorial(n - 1)
        
    def two_pointer_sum(arr, target):
        '''Two Pointer Technique: Finds if there exists a pair with the given sum.'''
        arr.sort()
        left, right = 0, len(arr) - 1
        while left < right:
            current_sum = arr[left] + arr[right]
            if current_sum == target:
                print(f"Pair found: {arr[left]}, {arr[right]}")
                return True
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return False
    
    def sliding_window_max_sum(arr, k):
        '''Sliding Window Technique: Finds the maximum sum of a subarray of size k.'''
        n = len(arr)
        if n < k:
            return -1

        max_sum = sum(arr[:k])
        current_sum = max_sum

        for i in range(k, n):
            current_sum += arr[i] - arr[i - k]
            max_sum = max(max_sum, current_sum)

        return max_sum
    
if __name__ == '__main__':
    arr = [1, 2, 4, 5, 7]
    arr1 = [3, 5, 6, 8, 9]
    num = 4
 