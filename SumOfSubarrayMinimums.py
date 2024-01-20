class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        result = 0
        n = len(arr)
        left = [-1]*n
        right = [n]*n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        for i in range(n):
            result += (i - left[i]) * (right[i] - i) * arr[i]
        return result % (10**9 + 7)

# Naive Approach:
# For all subarrays, track the minimum element.
# Add all minimum elements.
# Return the sum modulo 10^9 + 7.

# Code:
# class Solution:
#     def sumSubarrayMins(self, arr: List[int]) -> int:
#         # Time Complexity: O(n^2)
#         # Space Complexity: O(1)
#         result = 0
#         n = len(arr)
#         for i in range(n):
#             minimum = arr[i]
#             for j in range(i, n):
#                 minimum = min(minimum, arr[j])
#                 result += minimum
#         return result % (10**9 + 7)

# Time Complexity: O(n^2)
# Space Complexity: O(1)


# Optimization:
# Create two arrays left and right such that,
# left[i] --> the index of first strictly smaller number on the left of arr[i]
# right[i] --> the index of first smaller or equal number on the right of arr[i] 
# Then, for each element the number of subarrays in which arr[i] will be minimum can be obtained using (i - left[i]) x (right[i] - i)
# Multiply the number of subarrays with arr[i], and add in the result.
# Return result mod 10^9 + 7.

# Example:
# arr = [3, 1, 2, 4]
# For 3, first smaller element towards left = None (-1)
#        first smaller element towards right = 1 (index 1)
# Number of subarrays in which 3 is minimum = 0-(-1) * (1-0) = 1
# [3]
# For 1, first smaller element towards left = None (-1)
#        first smaller element towards right = None (index n)
# Number of subarrays in which 1 is minimum = 1-(-1) * (4-1) = 2x3 = 6
# [1], [3, 1], [1, 2], [3, 1, 2], [3, 1, 2, 4], [1, 2, 4]
# For 2, first smaller element towards left = 1 (index 1)
#        first smaller element towards right = None (index n)
# Number of subarrays in which 2 is minimum = 2-(1) * (4-2) = 2
# [2], [2, 4]
# For 4, first smaller element towards left = 2 (index 2)
#        first smaller element towards right = None (index n)
# Number of subarrays in which 4 is minimum = 3-(2) * (4-3) = 1
# [4]

# Code:
# class Solution:
#     def sumSubarrayMins(self, arr: List[int]) -> int:
#         # Time Complexity: O(n)
#         # Space Complexity: O(n)
#         result = 0
#         n = len(arr)
#         left = [-1]*n
#         right = [n]*n
#         stack = []
#         for i in range(n):
#             while stack and arr[stack[-1]] >= arr[i]:
#                 stack.pop()
#             if stack:
#                 left[i] = stack[-1]
#             stack.append(i)
#         stack = []
#         for i in range(n-1, -1, -1):
#             while stack and arr[stack[-1]] > arr[i]:
#                 stack.pop()
#             if stack:
#                 right[i] = stack[-1]
#             stack.append(i)
#         for i in range(n):
#             result += (i - left[i]) * (right[i] - i) * arr[i]
#         return result % (10**9 + 7)

# Time Complexity: O(n)
# Space Complexity: O(n)
