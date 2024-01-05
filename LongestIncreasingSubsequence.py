class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Binary Search
        # Time Complexity: O(nlogn)
        # Space Complexity: O(n)
        n = len(nums)
        if n == 0: return 0
        result = [nums[0]]
        length = 1
        for i in range(1, n):
            if nums[i] > result[-1]:
                result.append(nums[i])
                length += 1
            else:
                left = 0
                right = len(result) - 1
                while left < right:
                    mid = (left + right) // 2
                    if result[mid] >= nums[i]:
                        right = mid
                    else:
                        left = mid+1
                result[right] = nums[i]
        return length



# Brute force
# Generate all the subsequences (Recursion, Power Set) --> Check for increasing trend --> Return the longest
# For each element we can either take it or not take it in the LIS --> this will be based on the previous element in LIS --> for this we need to store the index of previous element in LIS.
# Starting at index = 0 and previndex = -1
# 1. We can take item at index i if, previndex == -1 or nums[previndex] < nums[i]: in that case increment the length by 1 and make previndex = i
# 2. We can not take the item at index i: in that case length and pevious both will remain same.
# Base condition will be when i == n --> in that case length will be 0.

# Code:
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         # Time Complexity: O(2^n)
#         # Space Complexity: O(n) stack space
#         n = len(nums)
#         return self.util(0, -1, n, nums)

#     def util(self, curr, prev, n, nums):
#         if curr == n:
#             return 0
#         maxVal = 0
#         if prev == -1 or nums[prev] < nums[curr]:
#             maxVal = max(1 + self.util(curr+1, curr, n, nums), maxVal)
#         maxVal = max(self.util(curr+1, prev, n, nums), maxVal)
#         return maxVal

# Time Complexity: O(2^n)
# Space Complexity: O(n) stack space



# Memoization:
# Create a table of size N x N+1, here, row indices represent current index and column indices store the prev index.
# Use this table to store values as we proceed with the recursive approach.
# This will reduce the time complexity to O(n^2).

# Code:
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         # Time Complexity: O(n^2)
#         # Space Complexity: O(n^2)
#         n = len(nums)
#         dp = [[-1]*(n+1) for i in range(n)]
#         return self.util(0, -1, n, nums, dp)

#     def util(self, curr, prev, n, nums, dp):
#         if curr == n: return 0
#         if dp[curr][prev+1] != -1: return dp[curr][prev+1]
#         length = self.util(curr+1, prev, n, nums, dp)
#         if prev == -1 or nums[prev] < nums[curr]:
#             length = max(length, 1 + self.util(curr+1, curr, n, nums, dp))
#         dp[curr][prev+1] = length
#         return length

# Time Complexity: O(n^2)
# Space Complexity: O(n^2) + O(n) due to spack space --> O(n^2)



# Tabulation
# Convert Memoization to Tabulation
# Code:
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         # Time Complexity: O(n^2)
#         # Space Complexity: O(n^2)
#         n = len(nums)
#         dp = [[0]*(n+1) for i in range(n+1)]
#         for curr in range(n-1, -1, -1):
#             for prev in range(curr-1, -2, -1):
#                 length = dp[curr+1][prev+1]
#                 if prev == -1 or nums[prev] < nums[curr]:
#                     length = max(length, 1 + dp[curr+1][curr+1])
#                 dp[curr][prev+1] = length
#         return dp[0][0]

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)



# Space Optimization
# nums = [10,9,2,5,3,7,101,18]
# dp = [_, _, _, _, _, _, _, _]
# for last element value in dp = 1
# dp = [_, _, _, _, _, _, _, 1]
# Next for 101 --> go back to all numbers greater than 101 --> as no element is greater than 101, value in dp = 1
# dp = [_, _, _, _, _, _, 1, 1]
# Next for 7 --> go back to all numbers greater than 7 --> as 101 and 18 both are greater, value in dp = max(val in 101, val in 18) + 1 = 2
# dp = [_, _, _, _, _, 2, 1, 1]
# Next for 3 --> go back to all numbers greater than 3 --> as 7, 101, and 18 all are greater, value in dp = max(val in 7, val in 101, val in 18) + 1 = 3
# dp = [_, _, _, _, 3, 2, 1, 1]
# Next for 5 --> go back to all numbers greater than 5 --> as 7, 101, and 18 are greater, value in dp = max(val in 7, val in 101, val in 18) + 1 = 3
# dp = [_, _, _, 3, 3, 2, 1, 1]
# Next for 2 --> go back to all numbers greater than 2 --> as 5, 3, 7, 101, and 18 all are greater, value in dp = max(val in 5, val in 3, val in 7, val in 101, val in 18) + 1 = 4
# dp = [_, _, 4, 3, 3, 2, 1, 1]
# Next for 9 --> go back to all numbers greater than 9 --> as 101 and 18 are greater, value in dp = max(val in 101, val in 18) + 1 = 2
# dp = [_, 2, 4, 3, 3, 2, 1, 1]
# Next for 10 --> go back to all numbers greater than 10 --> as 101 and 18 are greater, value in dp = max(val in 101, val in 18) + 1 = 2
# dp = [2, 2, 4, 3, 3, 2, 1, 1]

# length of the longest strictly increasing subsequence is the max number in dp --> 4

# Code:
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         # Time Complexity: O(n^2)
#         # Space Complexity: O(n) 
#         n = len(nums)
#         dp = [1]*n
#         for i in range(n-2, -1, -1):
#             nextmax = 0
#             for j in range(i+1, n):
#                 if nums[j] > nums[i]:
#                     nextmax = max(nextmax, dp[j])
#             dp[i] = nextmax + 1
#         return max(dp)

# Time Complexity: O(n^2)
# Space Complexity: O(n)



# Binary Search
# For each value we will find out if it can be added to an already existing increasing subsequence or we need to create a new increasing subsquence for it
# Example:
# nums = [10,9,2,5,3,7,101,18]
# for 10: create an increasing subsequence [10]
# for 9: create another increasing subsequence [10] [9]
# for 2: create another increasing subsequence [10] [9] [2]
# for 5: add it after 2, [10] [9] [2, 5]
# for 3: add it after 2, [10] [9] [2, 5] [2, 3]
# for 7: add it after 5 and 3, [10] [9] [2, 5, 7] [2, 3, 7]
# for 101: add it after all subsequences, [10, 101] [9, 101] [2, 5, 7, 101] [2, 3, 7, 101]
# for 18: add it after [10] [9] [2, 5, 7] [2, 3, 7], as [10, 101] [9, 101] [2, 5, 7, 101] [2, 3, 7, 101] [10, 18] [9, 18] [2, 5, 7, 18] [2, 3, 7, 18]
# so the length of longest increasing subsequence is 4.

# Instead of storing all the subsequences, we'll store then in a single array. If a value is larger than the last element of the array, we can simply append it at the end. Else, we'll look for the next greater element using binary search and replace it with the current element.

# Example:
# nums = [10,9,2,5,3,7,101,18]
# for 10: result = [10]
# for 9: result = [9]
# for 2: result = [2]
# for 5: result = [2, 5]
# for 3: result = [2, 3]
# for 7: result = [2, 3, 7]
# for 101: result = [2, 3, 7, 101]
# for 18: result = [2, 3, 7, 18]

# Note: The result may not always store the Longest Increasing Subsequence but its length is always equal to the length of longest increasing subsequence.

# Code:
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         # Time Complexity: O(nlogn)
#         # Space Complexity: O(n)
#         n = len(nums)
#         if n == 0: return 0
#         result = [nums[0]]
#         length = 1
#         for i in range(1, n):
#             if nums[i] > result[-1]:
#                 result.append(nums[i])
#                 length += 1
#             else:
#                 left = 0
#                 right = len(result) - 1
#                 while left < right:
#                     mid = (left + right) // 2
#                     if result[mid] >= nums[i]:
#                         right = mid
#                     else:
#                         left = mid+1
#                 result[right] = nums[i]
#         return length

# Time Complexity: O(nlogn)
# Space Complexity: O(n)
