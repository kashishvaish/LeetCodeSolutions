class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        n = len(nums)
        res = []
        for i in range(n):
            val = abs(nums[i])
            if nums[val-1] < 0:
                res.append(val)
            else:
                nums[val-1] *= -1
        return res
            
# Approach:
# Iterate through each number in the given list.
# For each number, get its absolute value since the number may have been negated in a previous iteration.
# Check if the number at the index corresponding to the absolute value (minus one) is negative. If it is negative, it means we have encountered this number before, so we add its absolute value to the result list.
# Otherwise, negate the number at the index corresponding to the absolute value (minus one) to mark its occurrence.
# Return the result list containing the duplicate numbers.

# Time Complexity: O(n), where n is the length of the input list. We iterate through the list once.
# Space Complexity: O(1) since we only use a constant amount of extra space for variables, and the space required for the result list is not counted.
