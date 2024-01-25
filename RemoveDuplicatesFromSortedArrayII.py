class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        n = len(nums)
        if n <= 2: return n
        k = 2
        secondlast = nums[0]
        last = nums[1]
        for i in range(2, n):
            if nums[i] != secondlast:
                nums[k] = nums[i]
                k += 1
            secondlast = last
            last = nums[i]
        return k

# Approach:
# The idea is to iterate through the array and maintain a pointer k that keeps track of the position where the next valid element should be placed.
# Two variables secondlast and last are used to keep track of the last two elements encountered, ensuring that the current element is not a duplicate of the previous two.

# Time Complexity: O(n)
# Space Complexity: O(1)
