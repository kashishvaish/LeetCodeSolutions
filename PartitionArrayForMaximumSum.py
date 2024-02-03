class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # Time Complexity: O(nk)
        # Space Complexity: O(n)
        n = len(arr)
        dp = [0]*(n+1)
        for i in range(n-1, -1, -1):
            currMax = arr[i]
            for j in range(i, min(i+k, n)):
                currMax = max(currMax, arr[j])
                dp[i] = max(dp[i], currMax * (j-i+1) + dp[j+1])
        return dp[0]

# Approach: Top-Down Dynamic Programming
# At each index, we decide the length of the subarray (from 1 to k) with that index as the starting point.
# Iterate over elements, maintaining the maximum value encountered (currMax).
# Assume each element in the subarray as the maximum value and calculate the sum.
# Recursively calculate the maximum sum for the remaining array after the subarray.
# Keep track of the maximum sum for each choice of subarray length.
# Memoize results to avoid redundant calculations.

# Code:
# class Solution:
#     def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
#         # Time Complexity: O(nk)
#         # Space Complexity: O(n)
#         n = len(arr)
#         dp = [-1]*n
#         return self.util(0, n, k, arr, dp)

#     def util(self, i, n, k, arr, dp):
#         if i == n: return 0
#         if dp[i] != -1: return dp[i]
#         currMax = arr[i]
#         ans = 0
#         for j in range(i, min(n, i+k)):
#             currMax = max(currMax, arr[j])
#             ans = max(ans, currMax * (j-i+1) + self.util(j+1, n, k, arr, dp))
#         dp[i] = ans
#         return ans

# Time Complexity: O(nk)
# Space Complexity: O(n)


# Approach: Bottom-Up Dynamic Programming
# Traverse the array in reverse order.
# Calculate and update the optimal sum for each subarray starting from the current index.
# At each step, identify the maximum element within the current subarray,
# and for each possible subarray length, calculate the sum, considering the contribution of the current subarray and the optimal sum for the remaining array.

# Code:
# class Solution:
#     def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
#         # Time Complexity: O(nk)
#         # Space Complexity: O(n)
#         n = len(arr)
#         dp = [0]*(n+1)
#         for i in range(n-1, -1, -1):
#             currMax = arr[i]
#             for j in range(i, min(i+k, n)):
#                 currMax = max(currMax, arr[j])
#                 dp[i] = max(dp[i], currMax * (j-i+1) + dp[j+1])
#         return dp[0]

# Time Complexity: O(nk)
# Space Complexity: O(n)
