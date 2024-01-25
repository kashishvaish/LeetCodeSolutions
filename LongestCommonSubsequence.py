class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Time Complexity: O(mxn)
        # Space Complexity: O(mxn)
        m = len(text1)
        n = len(text2)
        dp = [[0]*(n+1) for i in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]

# Dynamic Programming:
# The intuition behind the dynamic programming approach is to use a 2D array dp to store the lengths of LCS for various prefixes of the input strings.
# By comparing characters at each position, the algorithm fills up the dp array and computes the length of the LCS iteratively.

# Example: text1 = "abcde", text2 = "ace"
#     a c e
#   0 0 0 0
# a 0 1 1 1
# b 0 1 1 1
# c 0 1 2 2
# d 0 1 2 2
# e 0 1 2 3

# Time Complexity: O(mxn)
# Space Complexity: O(mxn)
