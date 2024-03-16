class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        n = len(nums)
        for i in range(n):
            if nums[i] == 0: nums[i] = -1
        maxlen = 0
        curr = 0
        d = {}
        for i in range(n):
            curr += nums[i]
            if curr == 0:
                maxlen = i+1
            elif curr in d:
                maxlen = max(maxlen, i - d[curr])
            else:
                d[curr] = i
        return maxlen

# Approach:
# Convert all 0s in the nums list to -1. This transformation is essential as it helps in simplifying the problem by treating 0s as -1s, which makes it easier to find subarrays with equal numbers of 0s and 1s.
# Initialize variables maxlen and curr to 0. maxlen will keep track of the maximum length of the subarray with equal numbers of 0s and 1s encountered so far, while curr will keep track of the cumulative sum of elements encountered while iterating through the nums list.
# Initialize an empty dictionary d to store the cumulative sums encountered along with their corresponding indices.
# Iterate through the nums list. For each element:
# Update curr by adding the current element's value to it.
# If curr equals 0, it indicates that all elements encountered so far from index 0 have equal numbers of 0s and 1s. Update maxlen to i+1, where i is the current index.
# If curr is already present in the dictionary d, it means there is a subarray with equal numbers of 0s and 1s between the current index and the index stored in d[curr]. Update maxlen by taking the maximum of its current value and i - d[curr].
# Otherwise, add curr to the dictionary d with the current index i.
# After iterating through the nums list, maxlen will hold the maximum length of the subarray with equal numbers of 0s and 1s. Return maxlen as the result.
    
# Time Complexity: O(n)
# Space Complexity: O(n)
