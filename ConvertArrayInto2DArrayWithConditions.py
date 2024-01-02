class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        n = len(nums)
        counts = [0]*(n+1)
        res = []
        maxfreq = 0
        for i in nums:
            if maxfreq <= counts[i]:
                res.append([])
            res[counts[i]].append(i)
            counts[i] += 1
            maxfreq = max(counts[i], maxfreq)
        return res

# Intuition:
# Create a list of length n+1 to store the frequencies of elements in nums.
# Create an empty list to store the result.
# For each integer i in nums -->
#   If the current max freq, is less than equal to the current frequency of i, add a row to the result list.
#   Append the integer i at the row with the index equal to current frequency of i.
#   Increase the frequency of i
#   Track the maximum frequency
# Return the result list

# Time Complexity: O(n)
# Space Complexity: O(n)
