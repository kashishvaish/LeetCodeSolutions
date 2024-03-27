class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        if k == 0: return 0
        n = len(nums)
        start = 0
        curr = 1
        result = 0
        for end in range(n):
            curr *= nums[end]
            while curr >= k and start <= end:
                curr //= nums[start]
                start += 1
            result += end-start+1
        return result
            
# Approach: Sliding Window
# Check if k is equal to 0. If so, return 0 because no subarray product will be less than or equal to 0.
# Get the length of the input list nums.
# Initialize variables: start to track the start index of the subarray, curr to store the product of elements within the current subarray, and result to count the number of valid subarrays.
# Iterate through the input list using the variable end as the end index of the subarray.
# Update the product of the current subarray by multiplying curr with the element at the end index.
# While the product curr is greater than or equal to k and the start index is less than or equal to the end index, adjust the subarray window by dividing curr by the element at the start index and incrementing the start index.
# Add the count of valid subarrays within the current window (end - start + 1) to the result.
# Repeat for all elements in the input list.
# Return the final result, which represents the total count of subarrays whose product is less than k.

# Time Complexity: O(n)
# Space Complexity: O(1)
