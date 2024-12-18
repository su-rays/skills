''' Given a string s, find the length of the longest substring without repeating characters. '''

def longest_substring_brute_force(s):
    max_length = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if len(set(s[i:j+1])) == (j - i + 1):  # All unique characters
                max_length = max(max_length, j - i + 1)
    return max_length

def longest_substring_greedy(s):
    max_length = 0
    start = 0
    char_index = {}
    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = i
        max_length = max(max_length, i - start + 1)
    return max_length

def longest_substring_divide_conquer(s):
    def helper(left, right):
        if left == right:
            return 1
        mid = (left + right) // 2
        left_len = helper(left, mid)
        right_len = helper(mid + 1, right)
        
        cross_len = 0
        seen = set()
        i = mid
        while i >= left and s[i] not in seen:
            seen.add(s[i])
            i -= 1
        j = mid + 1
        while j <= right and s[j] not in seen:
            seen.add(s[j])
            j += 1
        cross_len = len(seen)
        return max(left_len, right_len, cross_len)

    return helper(0, len(s) - 1)

def longest_substring_dp(s):
    dp = [0] * len(s)
    last_seen = {}
    max_length = 0
    for i, char in enumerate(s):
        if char not in last_seen:
            dp[i] = dp[i-1] + 1 if i > 0 else 1
        else:
            dp[i] = min(dp[i-1] + 1, i - last_seen[char])
        last_seen[char] = i
        max_length = max(max_length, dp[i])
    return max_length

def longest_substring_backtracking(s):
    def backtrack(start, current):
        nonlocal max_length
        max_length = max(max_length, len(current))
        for i in range(start, len(s)):
            if s[i] not in current:
                backtrack(i + 1, current + s[i])
    max_length = 0
    backtrack(0, "")
    return max_length

import random

def longest_substring_randomized(s):
    max_length = 0
    n = len(s)
    for _ in range(1000):  # Random trials
        start = random.randint(0, n - 1)
        end = random.randint(start, n - 1)
        if len(set(s[start:end+1])) == (end - start + 1):
            max_length = max(max_length, end - start + 1)
    return max_length

def longest_substring_recursion(s):
    def helper(start, seen):
        if start == len(s):
            return 0
        if s[start] in seen:
            return len(seen)
        seen.add(s[start])
        return max(len(seen), helper(start + 1, seen))
    return helper(0, set())

def longest_substring_two_pointer(s):
    start = 0
    max_length = 0
    seen = set()
    for end in range(len(s)):
        while s[end] in seen:
            seen.remove(s[start])
            start += 1
        seen.add(s[end])
        max_length = max(max_length, end - start + 1)
    return max_length

def longest_substring_sliding_window(s):
    window = {}
    max_length = start = 0
    for end, char in enumerate(s):
        if char in window and window[char] >= start:
            start = window[char] + 1
        window[char] = end
        max_length = max(max_length, end - start + 1)
    return max_length
