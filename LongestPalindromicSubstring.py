class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Time: O(n^2)
        # Space: O(n^2)
        n = len(s)
        if not n: return ""
        maxLen = 1
        start = 0
        dp = [[False]*n for i in range(n)]
        for i in range(n):
            dp[i][i] = True
            if i < n-1:
                if s[i] == s[i+1]:
                    dp[i][i+1] = True
                    if maxLen < 2:
                        maxLen = 2
                        start = i
        for l in range(2, n):
            for i in range(n-l):
                dp[i][i+l] = dp[i+1][i+l-1] and s[i] == s[i+l]
                if dp[i][i+l] and l+1 > maxLen:
                    maxLen = l+1
                    start = i
        return s[start: start+maxLen]
                
# Approach:

# 1. Brute Force Approach

# For every substring --> check whether it is palindrome or not --> return the max length palindromic string
# Time: O(n^3)
# Space: O(1)

# 2. Dynamic Programming

# Intuition: 
# String with length 1 --> always palindrome
# String with length 2 --> palindrome if both values are equal
# Else --> palindrome if (substring excluding first and last character is palindrome) and (first value == last value)
# Time: O(n^2)
# Space: O(n^2)
