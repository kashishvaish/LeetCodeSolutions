class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # Time Complexity: O(m + n)
        # Space Complexity: O(1)
        m = len(nums1)
        n = len(nums2)
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] == nums2[j]: return nums1[i]
            elif nums1[i] > nums2[j]: j += 1
            else: i += 1
        return -1

# Approach:
# Initialize two variables: i, which will store the position in nums1, and j, which will store the position in nums2 to 0, the starting index.
# Iterate through nums1 and nums2 while i is less than the size of nums1 and j is less than the size of nums2:
# If nums1[i] is less than nums2[j], increment i by 1 because we need a larger value from nums1 to match the value at nums2[j].
# If nums1[i] is greater than nums2[j], increment j by 1 because we need a larger value from nums2 to match the value at nums1[i].
# Otherwise, nums1[i] must equal nums2[j], so return the value of nums1[i]. We have found the minimum common value.
# Return -1 if the loop completes without returning an answer. This means there is no common value between nums1 and nums2.
    
# Time Complexity: O(m + n)
# Space Complexity: O(1)
