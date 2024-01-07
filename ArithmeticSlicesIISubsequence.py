from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # Time Complexity: O(n^2)
        # Space Complexity: O(n^2)
        n = len(nums)
        result = 0
        dp = [defaultdict(int) for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    result += dp[j][diff]
        return result                    



# Brute Force
# Generate all possible subsequences. --> Check if it is arithmetic or not. --> Return the number of total arithmetic subsequences.
# for each element we can either take or not take it.

# Code:
# class Solution:
#     def numberOfArithmeticSlices(self, nums: List[int]) -> int:
#         # Time Complexity: O(2^n)
#         # Space Complexity: O(n)
#         result = [0]
#         n = len(nums)
#         self.util(0, -1, 0, -1, n, nums, result)
#         return result[0]
#     def util(self, i, prev, count, diff, n, nums, result):
#         if i == n:
#             if count >= 3:
#                 result[0] += 1
#             return
#         self.util(i+1, prev, count, diff, n, nums, result)
#         if count == 0:
#             self.util(i+1, i, count+1, -1, n, nums, result)
#         elif count == 1:
#             self.util(i+1, i, count+1, nums[i]-nums[prev], n, nums, result)
#         elif diff == (nums[i]-nums[prev]):
#             self.util(i+1, i, count+1, diff, n, nums, result)

# Time Complexity: O(2^n)
# Space Complexity: O(n)



# Dynamic Programming
# [2,4,6,8,10]
# create an array of dictionaries of size n. --> the key of the dictionaries will be the common difference and the value will be the number of arithmetic subsequences with that common difference ending at that index i

# Code:
# from collections import defaultdict
# class Solution:
#     def numberOfArithmeticSlices(self, nums: List[int]) -> int:
#         # Time Complexity: O(n^2)
#         # Space Complexity: O(n^2)
#         n = len(nums)
#         result = 0
#         dp = [defaultdict(int) for i in range(n)]
#         for i in range(1, n):
#             for j in range(i):
#                 diff = nums[i] - nums[j]
#                 dp[i][diff] += 1
#                 if diff in dp[j]:
#                     dp[i][diff] += dp[j][diff]
#                     result += dp[j][diff]
#         return result

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
