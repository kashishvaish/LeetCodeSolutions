class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        target = max(nums)
        curr = 0
        start = 0
        n = len(nums)
        result = 0
        for end in range(n):
            if nums[end] == target: curr += 1
            while curr == k:
                if nums[start] == target: curr -= 1
                start += 1
            result += start
        return result
    
# Approach:   
# Initialize variables: target to store the maximum value in the list nums, curr to count the occurrences of target in the current subarray, start to track the start index of the current subarray, n to store the length of the input list nums, and result to accumulate the count of valid subarrays.
# Iterate through the list nums using the variable end as the end index of the current subarray.
# If the current element nums[end] is equal to the target, increment the curr count.
# While the curr count is equal to k, implying that the current subarray has exactly k occurrences of target:
# If the element at the start index is equal to the target, decrement the curr count.
# Increment the start index to move to the next subarray.
# Add the value of the start index to the result to count all subarrays that satisfy the condition.
# Repeat steps 2-5 for all elements in the input list.
# Return the final result, which represents the count of valid subarrays.

# Time Complexity: O(n)
# Space Complexity: O(1)
