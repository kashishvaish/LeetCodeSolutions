class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Time Complexity: O(m+n)
        # Space Complexity: O(m+n)
        setA = set(nums1)
        setB = set(nums2)
        result = []
        for num in setA:
            if num in setB: result.append(num)
        return result

# Approach:
# Begin by converting the input lists nums1 and nums2 into sets setA and setB, respectively. This operation eliminates any duplicate elements in each list, resulting in sets containing unique elements.
# Initialize an empty list result to store the intersection of the two sets.
# Iterate through each element num in setA. For each element, check if it also exists in setB. If it does, append num to the result list.
# After iterating through all elements in setA, result will contain all the elements that are common to both sets setA and setB, representing the intersection of the two input lists.
# Finally, return the result list.

# Time Complexity: O(m+n)
# Space Complexity: O(m+n)
