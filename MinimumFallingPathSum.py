class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # Time Complexity: O(n^2)
        # Space Complexity: O(n)
        n = len(matrix)
        prev = [i for i in matrix[0]]
        curr = [-1]*n
        for row in range(1, n):
            for col in range(n):
                minimum = prev[col]
                if col-1 >= 0:
                    minimum = min(prev[col-1], minimum)
                if col+1 < n:
                    minimum = min(prev[col+1], minimum)
                curr[col] = matrix[row][col] + minimum
            prev = [i for i in curr]
        return min(prev)

# Dynamic Programming:
# Create a table dp of size n x n.
# dp[i][j] should store the minimum sum of any falling path ending at dp[i][j].

# Code:
# class Solution:
#     def minFallingPathSum(self, matrix: List[List[int]]) -> int:
#         # Time Complexity: O(n^2)
#         # Space Complexity: O(n^2)
#         n = len(matrix)
#         dp = [[-1]*n for i in range(n)]
#         for i in range(n):
#             dp[0][i] = matrix[0][i]
#         for row in range(1, n):
#             for col in range(n):
#                 minimum = dp[row-1][col]
#                 if col-1 >= 0:
#                     minimum = min(dp[row-1][col-1], minimum)
#                 if col+1 < n:
#                     minimum = min(dp[row-1][col+1], minimum)
#                 dp[row][col] = matrix[row][col] + minimum
#         return min(dp[-1])

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)


# Space Optimization:
# We know that we only need values from previous row to get the current row, so we can just store the previous and current rows.

# Code:
# class Solution:
#     def minFallingPathSum(self, matrix: List[List[int]]) -> int:
#         # Time Complexity: O(n^2)
#         # Space Complexity: O(n)
#         n = len(matrix)
#         prev = [i for i in matrix[0]]
#         curr = [-1]*n
#         for row in range(1, n):
#             for col in range(n):
#                 minimum = prev[col]
#                 if col-1 >= 0:
#                     minimum = min(prev[col-1], minimum)
#                 if col+1 < n:
#                     minimum = min(prev[col+1], minimum)
#                 curr[col] = matrix[row][col] + minimum
#             prev = [i for i in curr]
#         return min(prev)

# Time Complexity: O(n^2)
# Space Complexity: O(n)
