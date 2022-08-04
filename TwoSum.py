class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time: O(n)  Space: O(n)
        hashMap = {}
        for i, num in enumerate(nums):
            if target-num in hashMap:
                return [hashMap[target-num], i]
            hashMap[num] = i
        return [-1, -1]
        
# Approach

# 1. Brute Force Approach

# For all possible pairs, find their sum --> if sum == target for a pair: return indices of those elements.
# Time: O(n^2)
# Space: O(1)

# 2. Using HashMap

# Store elements and their indices as key and pairs in a HashMap, while traversing through the vector --> if target - element is present in the HashMap --> return index of target-element and element.
# Time: O(n)
# Space: O(n)
