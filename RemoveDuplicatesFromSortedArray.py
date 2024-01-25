class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        n = len(nums)
        k = 1
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k

# Approach:
# Iterate through the input array nums and maintain a separate index k to keep track of the position where the next unique element should be placed. By comparing each element with its previous one, the code identifies duplicates and updates the array in-place, ensuring that only unique elements are present.

# Time Complexity: O(n)
# Space Complexity: O(1)
