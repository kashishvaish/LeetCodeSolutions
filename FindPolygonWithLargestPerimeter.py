class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # Time Complexity: O(nlogn)
        # Space Complexity: O(n)
        n = len(nums)
        nums.sort()
        total = sum(nums)
        for k in range(n-1, 1, -1):
            if total - nums[k] >  nums[k]:
                return total
            total -= nums[k]
        return -1

        
# Approach:
# Sort the input list nums in ascending order.
# Store the sum of nums in a variable total.
# Iterate through the sorted list in reverse order, starting from the largest integer to the third integer.
# For each iteration, check if total - nums[k] is greater than nums[k]. This condition is essential for a valid polygon.
    # If the condition is satisfied, it means a valid polygon can be formed, and the function returns the sum of all integers in the list (total), which represents the largest possible perimeter.
    # Else, we'll remove the largest side from our polygon by subtracting nums[k] from total.
# If no valid polygon can be formed, return -1.

# Example:
# nums = [1,12,1,2,5,50,3]
# nums = [1,1,2,3,5,12,50]
# 1+1+2+3+5+12 < 50
# remove 50
# 1+1+2+3+5 = 12
# remove 12
# 1+1+2+3 > 5
# possible
# parameter = 12

# Time Complexity: O(nlogn)
# Space Complexity: O(n)
