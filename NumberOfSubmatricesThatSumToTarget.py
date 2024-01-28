class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # Time Complexity: O(m x n^2)
        # Space Complexity: O(mn)
        m = len(matrix)
        n = len(matrix[0]) 
        result = 0
        for x in range(m):
            for y in range(1, n):
                matrix[x][y] += matrix[x][y-1]
        
        for c1 in range(n):
            for c2 in range(c1, n):
                map = {0: 1}
                sum = 0
                for row in range(m):
                    sum += matrix[row][c2] - (matrix[row][c1-1] if c1 > 0 else 0)
                    if sum-target in map:
                        result += map[sum-target]
                    map[sum] = map.get(sum, 0) + 1

        return result % (10**9 + 7)



# Naive Approach:
# Use nested loops to iterate through all possible submatrices. For each submatrix, calculate the sum of elements within the submatrix and increment the result if the sum matches the target.

# Code:
# class Solution:
#     def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
#         # Time Complexity: O(m^3 x n^3)
#         # Space Complexity: O(1)
#         m = len(matrix)
#         n = len(matrix[0]) 
#         result = 0
#         for x1 in range(m):
#             for y1 in range(n):
#                 for x2 in range(x1, m):
#                     for y2 in range(y1, n):
#                         sum = 0
#                         for x in range(x1, x2+1):
#                             for y in range(y1, y2+1):
#                                 sum += matrix[x][y]
#                         if sum == target: result += 1
#         return result % (10**9 + 7)

# Time Complexity: O(m^3 x n^3)
# Space Complexity: O(1)



# Dynamic Programming
# Use a 2D array dp to store the cumulative sums of submatrices, reducing the time complexity for sum calculations.

# Code:
# class Solution:
#     def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
#         # Time Complexity: O(m^2 x n^2)
#         # Space Complexity: O(mn)
#         m = len(matrix)
#         n = len(matrix[0]) 
#         result = 0
#         for x1 in range(m):
#             for y1 in range(n):
#                 dp = [[0]*n for i in range(m)]
#                 for x2 in range(x1, m):
#                     for y2 in range(y1, n):
#                         if x2 == x1 and y2 == y1: dp[x2][y2] = matrix[x2][y2];
#                         elif x2 == x1: dp[x2][y2] = dp[x2][y2-1] + matrix[x2][y2];
#                         elif y2 == y1: dp[x2][y2] = dp[x2-1][y2] + matrix[x2][y2];
#                         else: dp[x2][y2] = dp[x2][y2-1] + dp[x2-1][y2] - dp[x2-1][y2-1] + matrix[x2][y2];
#                         if dp[x2][y2] == target: result += 1
#         return result % (10**9 + 7)

# Time Complexity: O(m^2 x n^2)
# Space Complexity: O(mn)



# Prefix Sum
# Iterate through each row and precompute the cumulative sum for each element in that row.
# Then, for each pair of columns, scan through rows to compute submatrix sums, eliminating the need for nested loops over each element. The map keeps track of encountered sums, making it easy to identify submatrices with the target sum.

# Code:
# class Solution:
#     def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
#         # Time Complexity: O(m x n^2)
#         # Space Complexity: O(mn)
#         m = len(matrix)
#         n = len(matrix[0]) 
#         result = 0
#         for x in range(m):
#             for y in range(1, n):
#                 matrix[x][y] += matrix[x][y-1]
        
#         for c1 in range(n):
#             for c2 in range(c1, n):
#                 map = {0: 1}
#                 sum = 0
#                 for row in range(m):
#                     sum += matrix[row][c2] - (matrix[row][c1-1] if c1 > 0 else 0)
#                     if sum-target in map:
#                         result += map[sum-target]
#                     map[sum] = map.get(sum, 0) + 1

#         return result % (10**9 + 7)

# Time Complexity: O(m x n^2)
# Space Complexity: O(mn)
