class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        n = len(nums)
        res = []
        countNeg = 0
        for i in range(n):
            if nums[i] < 0:
                countNeg += 1
            else: break
        if countNeg == n: i = n
        j = countNeg - 1
        while i < n and j >= 0:
            if nums[i] < abs(nums[j]):
                res.append(nums[i]**2)
                i += 1
            else:
                res.append(nums[j]**2)
                j -= 1
        while i < n:
            res.append(nums[i]**2)
            i += 1
        while j >= 0:
            res.append(nums[j]**2)
            j -= 1
        return res

# Approach:
# First, traverse the given list of integers, counting the number of negative numbers encountered.
# Then, initialize two pointers: one starting from the first positive number and another starting from the last negative number.
# While iterating through the list with these pointers, compare the absolute values of the negative and positive numbers.
# Append the square of the smaller absolute value to the result list.
# After completing this process, any remaining positive or negative numbers are added to the result list accordingly. 

# Time Complexity: O(n)
# Space Complexity: O(n)
