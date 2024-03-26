class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        n = len(nums)
        for i in range(n):
            if nums[i] < 1 or nums[i] > n: nums[i] = n+1
        for i in range(n):
            val = abs(nums[i])
            if val == n+1: continue
            if nums[val-1] > 0: nums[val-1] *= -1
        for i in range(n):
            if nums[i] > 0: return i+1
        return n+1
        
# Approach:
# Total elements = n, so the answer would be in range 1 to n+1.
# We can use the indexes to store the occurence of a value.

# Iterate through each number in the given list.
# For each number, check if it is less than 1 or greater than n (where n is the length of the input list). If so, set it to n+1. This step ensures that only positive numbers within the range [1, n] are considered for finding the first missing positive integer.
# Iterate through the list again.
# For each number, get its absolute value since the number may have been negated in a previous iteration.
# If the absolute value is n+1, continue to the next iteration since it indicates a number outside the range of interest.
# Negate the number at the index corresponding to the absolute value (minus one) to mark its occurrence.
# Iterate through the list once more.
# For each number, if it is positive, return its index plus one as it indicates the first missing positive integer.
# If no positive number is found, return n+1, indicating that all integers in the range [1, n] are present in the list, and the first missing positive integer is n+1.

# Time Complexity: O(n), where n is the length of the input list. We iterate through the list three times, each time in O(n) complexity.
# Space Complexity: O(1) since we only use a constant amount of extra space for variables.
