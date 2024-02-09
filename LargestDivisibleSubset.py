class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # Time complexity: O(n^2)
        # Space complexity: O(n)
        n = len(nums)
        nums.sort()
        groupSize = [1] * n
        prevElement = [-1] * n
        maxIndex = 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if groupSize[i] < 1 + groupSize[j]:
                        groupSize[i] = 1 + groupSize[j]
                        prevElement[i] = j
            if groupSize[i] > groupSize[maxIndex]:
                maxIndex = i
        result = []
        while maxIndex != -1:
            result.insert(0, nums[maxIndex])
            maxIndex = prevElement[maxIndex]
        return result

# Time complexity: O(n^2)
# Space complexity: O(n)
