class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # Time Complexity: O(m x n x maxMove)
        # Space Complexity: O(m x n)
        dp = [[0]*n for i in range(m)]
        dp[startRow][startColumn] = 1
        result = 0
        for i in range(1, maxMove+1):
            temp = [[0]*n for i in range(m)]
            for row in range(m):
                for col in range(n):
                    if row == 0:
                        result += dp[row][col]
                    if col == 0:
                        result += dp[row][col]
                    if row == m-1:
                        result += dp[row][col]
                    if col == n-1:
                        result += dp[row][col]
                    if row-1 >= 0: temp[row][col] += dp[row-1][col]
                    if col-1 >= 0: temp[row][col] += dp[row][col-1]
                    if row+1 < m: temp[row][col] += dp[row+1][col]
                    if col+1 < n: temp[row][col] += dp[row][col+1]
            dp = temp
        return result % (10**9 + 7)


# Naive Approach
# The problem can be approached using a recursive depth-first search (DFS) strategy.
# The idea is to explore all possible moves of the ball in the grid and count the paths that lead to moving the ball out of the grid boundary within the given maximum number of moves.

# Code:
# class Solution:
#     def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
#         # Time Complexity: O(4^maxMove)
#         # Space Complexity: O(maxMove)
#         result = self.util(m, n, maxMove, startRow, startColumn, 0)
#         return result % (10**9 + 7)

#     def util(self, m, n, maxMove, row, col, i):
#         if(row < 0 or row >= m or col < 0 or col >= n):
#             return 1
#         if(i == maxMove): return 0
#         ans = self.util(m, n, maxMove, row+1, col, i+1) + self.util(m, n, maxMove, row-1, col, i+1) + self.util(m, n, maxMove, row, col+1, i+1) + self.util(m, n, maxMove, row, col-1, i+1)
#         return ans

# Time Complexity: O(4^maxMove)
# Space Complexity: O(maxMove)



# Recursion with Memoization
# The idea is to use a 3D array dp to store intermediate results, avoiding redundant computations during recursive calls.
# This helps in reducing the time complexity compared to the purely recursive solution.

# Code:
# class Solution:
#     def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
#         # Time Complexity: O(m x n x maxMove)
#         # Space Complexity: O(m x n x maxMove)
#         dp = [[[-1]*(maxMove+1) for i in range(n)] for j in range(m)]
#         result = self.util(m, n, maxMove, startRow, startColumn, 0, dp)
#         return result % (10**9 + 7)

#     def util(self, m, n, maxMove, row, col, i, dp):
#         if(row < 0 or row >= m or col < 0 or col >= n):
#             return 1
#         if(i == maxMove): return 0
#         if dp[row][col][i] != -1: return dp[row][col][i]
#         ans = self.util(m, n, maxMove, row+1, col, i+1, dp) + self.util(m, n, maxMove, row-1, col, i+1, dp) + self.util(m, n, maxMove, row, col+1, i+1, dp) + self.util(m, n, maxMove, row, col-1, i+1, dp)
#         dp[row][col][i] = ans
#         return ans

# Time Complexity: O(m x n x maxMove)
# Space Complexity: O(m x n x maxMove)



# Dynamic Programming
# The approach involves maintaining a 2D array dp of size m x n to represent the number of ways the ball can reach each cell in the grid after a certain number of moves.
# The result is accumulated by considering the edges of the grid in each iteration.

# Example: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
#  O _
#  _ _

# move = 0
# 1 0
# 0 0

# move = 1
# 1 1
# 1 0

# move = 2
# (0, 0) --> 1 ball and can go out in two ways = 2
# (0, 1) --> 1 ball and can go out in two ways = 2
# (1, 0) --> 1 ball and can go out in two ways = 2
# (0, 0) --> 0 ball and can go out in two ways = 0

# Ways: 2 + 2 + 2 + 0 = 6

# Code:
# class Solution:
#     def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
#         # Time Complexity: O(m x n x maxMove)
#         # Space Complexity: O(m x n)
#         dp = [[0]*n for i in range(m)]
#         dp[startRow][startColumn] = 1
#         result = 0
#         for i in range(1, maxMove+1):
#             temp = [[0]*n for i in range(m)]
#             for row in range(m):
#                 for col in range(n):
#                     if row == 0:
#                         result += dp[row][col]
#                     if col == 0:
#                         result += dp[row][col]
#                     if row == m-1:
#                         result += dp[row][col]
#                     if col == n-1:
#                         result += dp[row][col]
#                     if row-1 >= 0: temp[row][col] += dp[row-1][col]
#                     if col-1 >= 0: temp[row][col] += dp[row][col-1]
#                     if row+1 < m: temp[row][col] += dp[row+1][col]
#                     if col+1 < n: temp[row][col] += dp[row][col+1]
#             dp = temp
#         return result % (10**9 + 7)

# Time Complexity: O(m x n x maxMove)
# Space Complexity: O(m x n)
