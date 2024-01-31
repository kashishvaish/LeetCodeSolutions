class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        n = len(temperatures)
        result = [0]*n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            if stack:
                result[i] = stack[-1][1] - i
            stack.append((temperatures[i], i))
        return result

# Naive Approach:
# For each index i,
# Traverse the index from i+1 to n, to search next greater temperature.

# Code:
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         # Time Complexity: O(n^2)
#         # Space Complexity: O(n)
#         n = len(temperatures)
#         result = [0]*n
#         for i in range(n):
#             for j in range(i+1, n):
#                 if temperatures[j] > temperatures[i]:
#                     result[i] = j-i
#                     break
#         return result

# Time Complexity: O(n^2)
# Space Complexity: O(n)


# Using Stack:
# Iterate through the temperatures in reverse order, starting from the last day.
# Use a stack to keep track of the temperatures and their corresponding indices.
# For each temperature, compare it with the temperatures in the stack.
# Pop temperatures from the stack until we find a warmer day or until the stack is empty.
# If the stack is not empty after the while loop 
# --> There is a warmer day for the current temperature.
# --> Update the result for that day.
# Finally, push the current temperature and its index onto the stack.

# Code:
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         # Time Complexity: O(n)
#         # Space Complexity: O(n)
#         n = len(temperatures)
#         result = [0]*n
#         stack = []
#         for i in range(n-1, -1, -1):
#             while stack and stack[-1][0] <= temperatures[i]:
#                 stack.pop()
#             if stack:
#                 result[i] = stack[-1][1] - i
#             stack.append((temperatures[i], i))
#         return result

# Time Complexity: O(n)
# Space Complexity: O(n)
