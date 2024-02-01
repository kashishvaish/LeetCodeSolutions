class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        # Time Complexity: O(nlogn)
        # Space Complexity: O(n)
        n = len(nums)
        nums.sort()
        res = []
        for i in range(0, n, 3):
            if(nums[i+2] - nums[i] <= k):
                res.append(nums[i:i+3])
            else:
                return []
        return res

# Approach:
# Sort the array in ascending order.
# Iterate through the sorted array in steps of 3.
# For each group of three consecutive elements,
#   Check if maximum - minimum <= k.
#   If yes, append the current group to the result list.
#   Else, immediately return an empty list, indicating that it's not possible to divide the array as required.
# Finally, return the resulting list of subarrays.

# Time Complexity: O(nlogn)
# Space Complexity: O(n)
