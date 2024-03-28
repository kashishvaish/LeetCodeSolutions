class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        n = len(nums)
        d = {}
        result = 0
        start = 0
        for end in range(n):
            d[nums[end]] = d.get(nums[end], 0) + 1
            while d[nums[end]] > k:
                d[nums[start]] -= 1
                start += 1
            result = max(result, end-start+1)
        return result

# Approach:
# Initialize the length of the input list nums, an empty dictionary d to store the frequency of each element, and a variable result to track the maximum length of a good subarray.
# Initialize a variable start to keep track of the start index of the current subarray.
# Iterate through the input list nums using the variable end as the end index of the subarray.
# Update the frequency count of the current element nums[end] in the dictionary d.
# While the frequency count of the current element exceeds k, decrease the frequency count of the element at the start index and increment the start index until the frequency count becomes less than or equal to k.
# Update the result to be the maximum of the current result and the length of the current subarray (end - start + 1).
# Return the final result, which represents the length of the longest good subarray.
    
# Time Complexity: O(n)
# Space Complexity: O(n)
