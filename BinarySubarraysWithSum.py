class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        start = 0
        preZeros = 0
        currSum = 0
        totalCount = 0
        n = len(nums)
        for end in range(n):
            currSum += nums[end]
            while start < end and (nums[start] == 0 or currSum > goal):
                if nums[start] == 1:
                    preZeros = 0
                else:
                    preZeros += 1
                currSum -= nums[start]
                start += 1
            if currSum == goal:
                totalCount += 1 + preZeros
        return totalCount

# Approach:
# Initialize variables start, prefixZeros, currentSum, and totalCount to 0.
# Iterate through the array using the end variable as the end index of the sliding window.
# Add the current element to the currentSum.
# Enter a while loop to shrink the window from the left side if the sum exceeds the goal or if the element at the start of the window is 0.
# Inside the while loop, check if the element at the start of the window is 1. If it is, reset the prefixZeros count to 0. Otherwise, increment the prefixZeros count.
# Then subtract the element at the start of the window from the currentSum and increment the start pointer to move the window.
# If the currentSum is equal to the goal, increment the totalCount by 1 plus the prefixZeros count.
# Finally, return the totalCount.
      
# Time Complexity: O(n)
# Space Complexity: O(1)
