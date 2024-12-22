import random

class LongestSubstr:
    def __init__(self, string):
        self.string = string

    def brute_force(self):
        str_len = len(self.string)
        max_substr_len = 0
        max_substr = ''
        for i in range(str_len):
            for j in range(i, str_len):
                unique_substr = set(self.string[i:j+1])
                if len(unique_substr) == j-i+1:
                    if j-i+1 > max_substr_len:
                        max_substr_len = j-i+1
                        max_substr = self.string[i:j+1]
        return max_substr_len, max_substr
    
    
    def greedy(self):
        max_length = 0
        start = 0
        char_index = {}
        longest_substr = ""
        for i, char in enumerate(self.string):
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            char_index[char] = i
            if i - start + 1 > max_length:
                max_length = i - start + 1
                longest_substr = self.string[start:i + 1]
        return max_length, longest_substr
    
    def divide_conquer(self):
        def helper(left, right):
            if left == right:
                return 1, self.string[left]
            
            mid = (left + right) // 2
            left_len, left_substr = helper(left, mid)
            right_len, right_substr = helper(mid + 1, right)
            
            seen = set()
            i, j = mid, mid + 1
            cross_substr = ""
            while i >= left and self.string[i] not in seen:
                cross_substr = self.string[i] + cross_substr
                seen.add(self.string[i])
                i -= 1
            while j <= right and self.string[j] not in seen:
                cross_substr += self.string[j]
                seen.add(self.string[j])
                j += 1
            
            cross_len = len(cross_substr)
            if left_len >= right_len and left_len >= cross_len:
                return left_len, left_substr
            elif right_len >= left_len and right_len >= cross_len:
                return right_len, right_substr
            else:
                return cross_len, cross_substr

        max_length, substr = helper(0, len(self.string) - 1)
        return max_length, substr
    
    def dynamic_programming(self):
        n = len(self.string)
        if n == 0:
            return 0, ""
        
        dp = [0] * n
        last_seen = {}
        max_length = 0
        max_substr = ""
        for i, char in enumerate(self.string):
            if char not in last_seen:
                dp[i] = dp[i - 1] + 1 if i > 0 else 1
            else:
                dp[i] = min(dp[i - 1] + 1, i - last_seen[char])
            last_seen[char] = i
            if dp[i] > max_length:
                max_length = dp[i]
                max_substr = self.string[i - max_length + 1:i + 1]
        return max_length, max_substr
    
    def backtracking_recursion(self):
        def backtrack(start, used_chars):
            nonlocal max_length, max_substr
            current = ""
            for i in range(start, len(self.string)):
                char = self.string[i]
                if char in used_chars:
                    break
                current += char
                used_chars.add(char)
                if len(current) > max_length:
                    max_length = len(current)
                    max_substr = current

            for i in range(start + 1, len(self.string)):
                backtrack(i, set())

        max_length = 0
        max_substr = ""
        backtrack(0, set())
        return max_length, max_substr
    
    def randomized(self):
        max_length = 0
        max_substr = ""
        n = len(self.string)

        for _ in range(1000):
            start = random.randint(0, n - 1)
            end = random.randint(start, n - 1)
            substr = self.string[start:end + 1]

            if len(set(substr)) == len(substr):
                if len(substr) > max_length:
                    max_length = len(substr)
                    max_substr = substr

        fallback_length, fallback_substr = self.sliding_window()
        if fallback_length > max_length:
            return fallback_length, fallback_substr

        return max_length, max_substr

    def two_pointer(self):
        start = 0
        max_length = 0
        seen = set()
        longest_substr = ""
        for end in range(len(self.string)):
            while self.string[end] in seen:
                seen.remove(self.string[start])
                start += 1
            seen.add(self.string[end])
            if end - start + 1 > max_length:
                max_length = end - start + 1
                longest_substr = self.string[start:end + 1]
        return max_length, longest_substr
    
    def sliding_window(self):
        window = {}
        max_length = start = 0
        longest_substr = ""
        for end, char in enumerate(self.string):
            if char in window and window[char] >= start:
                start = window[char] + 1
            window[char] = end
            if end - start + 1 > max_length:
                max_length = end - start + 1
                longest_substr = self.string[start:end + 1]
        return max_length, longest_substr
    


if __name__ == "__main__":
    string = "GEEKSFORGEEKS"
    lgsubstr = LongestSubstr(string)
    substrlen, substr = lgsubstr.backtracking_recursion()
    print(f"Length of longest substr for string {string} is {substrlen}: {substr}")