from bisect import bisect_right

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Time Complexity: O(nlogn)
        # Space Complexity: O(n)
        n = len(profit)
        data = list(zip(startTime, endTime, profit))
        data.sort(key= lambda x: x[1])
        dp = [0]*(n+1)
        for i in range(n):
            prev = bisect_right(data, data[i][0], hi=i, key=lambda x: x[1])
            dp[i+1] = max(dp[i], data[i][2] + dp[prev])
        return dp[n]



# Intuition:

# Recursion:
# startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
# (1, 3, 50) (2, 4, 10) (3, 5, 40) (3, 6, 70)

# Order in the basis of increasing end time
# For each job option 1: take,  option 2: not take
# curr time = 0
# For (1, 3, 50)  --> take: curr time = 3 and profit = 50
                # --> not take: curr time = 0 and profit = 0

# For (2, 4, 10) --> If we take first job, curr time becomes 3, so we can't take second job --> current time remains = 3 and profit = 50
# If we do not take first job, curr time remains 0, so either we can take second job then --> current time = 4 and profit = 10
# Else we can choose to not take second job as well --> curr time = 0 and profit = 0

# For (3, 5, 40) --> 1. current time = 3 and profit = 50 -->
#   a) take -->  current time = 5 and profit = 90
#   b) not take --> current time = 3 and profit = 50
# 2. current time = 4 and profit = 10 -->
#   a) can't take --> current time = 4 and profit = 10
# 3. curr time = 0 and profit = 0 -->
#   a) take -->  current time = 5 and profit = 40
#   b) not take --> current time = 0 and profit = 0

# For (3, 6, 70) --> 1. current time = 5 and profit = 90 -->
#   a) can't take --> current time = 5 and profit = 90
# 2. current time = 3 and profit = 50 -->
#   a) take -->  current time = 6 and profit = 120
#   b) not take --> current time = 3 and profit = 50
# 3. current time = 4 and profit = 10 -->
#   a) can't take --> current time = 4 and profit = 10
# 4. current time = 5 and profit = 40 -->
#   a) can't take --> current time = 5 and profit = 40
# 5. current time = 0 and profit = 0 -->
#   a) take -->  current time = 6 and profit = 70
#   b) not take --> current time = 0 and profit = 0

# answer is max profit --> 120

# Code:
# class Solution:
#     def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
#         # Time Complexity: O(2^n)
#         # Space Complexity: O(n)
#         n = len(profit)
#         data = list(zip(startTime, endTime, profit))
#         data.sort(key= lambda x: x[1])
#         return self.util(0, 0, 0, n, data)

#     def util(self, i, currtime, profit, n, data):
#         if i == n:
#             return profit
#         temp = self.util(i+1, currtime, profit, n, data)
#         if currtime <= data[i][0]:
#             temp = max(temp, self.util(i+1, data[i][1], profit+data[i][2], n, data))
#         return temp

# Time Complexity: O(2^n)
# Space Complexity: O(n)



# Dynamic Programming:

# Example 1:
# startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
# (1, 3, 50) (2, 4, 10) (3, 5, 40) (3, 6, 70)
# For (1, 3, 50) --> no non conflicting job before --> total profit = 50, dp[0] = 50
# For (2, 4, 10) --> no non conflicting job before --> total profit = 10, dp[1] = 10
# For (3, 5, 40) --> non conflicting job before = (1, 3, 50) [profit = dp[0] = 50] --> total profit = 40 + 50 = 90
# For (3, 6, 70) --> non conflicting jobs before = (1, 3, 50) [profit = dp[0] = 50] --> total profit = 70 + 50 = 120
# dp = [50, 10, 90, 120]
# max profit = 120

# Example 2:
# startTime = [1,2,3,4,6]
# endTime = [3,5,10,6,9]
# profit = [20,20,100,70,60]
# (1, 3, 20) (2, 5, 20) (4, 6, 70) (6, 9, 60) (3, 10, 100)
# dp = [20, 20, 90, 150, 120]
# max profit = 150

# Code:
# class Solution:
#     def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
#         # Time Complexity: O(n^2)
#         # Space Complexity: O(n)
#         n = len(profit)
#         data = list(zip(startTime, endTime, profit))
#         data.sort(key= lambda x: x[1])
#         dp = [0]*n
#         dp[0] = data[0][2]
#         for i in range(1, n):
#             prev = -1
#             for j in range(i-1, -1, -1):
#                 if data[i][0] >= data[j][1]:
#                     prev = j
#                     break
#             dp[i] = max(dp[i-1], data[i][2] + dp[prev])
#         return dp[-1]

# Time Complexity: O(n^2)
# Space Complexity: O(n)



# Binary Search
# Reduce search space using binary search to improve time complexity.

# Code:
# from bisect import bisect_right

# class Solution:
#     def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
#         # Time Complexity: O(nlogn)
#         # Space Complexity: O(n)
#         n = len(profit)
#         data = list(zip(startTime, endTime, profit))
#         data.sort(key= lambda x: x[1])
#         dp = [0]*(n+1)
#         for i in range(n):
#             prev = bisect_right(data, data[i][0], hi=i, key=lambda x: x[1])
#             dp[i+1] = max(dp[i], data[i][2] + dp[prev])
#         return dp[n]

# Time Complexity: O(nlogn)
# Space Complexity: O(n)
