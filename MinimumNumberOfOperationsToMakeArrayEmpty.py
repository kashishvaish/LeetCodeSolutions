class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        counts = {}
        for i in nums:
            counts[i] = counts.get(i, 0) + 1
        total = 0
        for freq in counts.values():
            if freq == 1: return -1
            total += ceil(freq / 3)
        return total

# Intuition:
# For freq 1 --> return -1
# For freq 2 --> moves required are 1 (2)
# For freq 3 --> moves required are 1 (3)
# For freq 4 --> moves required are 2 (2 2)
# For freq 5 --> moves required are 2 (2 3)
# For freq 6 --> moves required are 2 (3 3)
# For freq 7 --> moves required are 3 (2 2 3)
# For freq 8 --> moves required are 3 (2 3 3)
# For freq 9 --> moves required are 3 (3 3 3)
# For freq 10 --> moves required are 4 (2 2 3 3)
# For freq 11 --> moves required are 4 (2 3 3 3)
# For freq 12 --> moves required are 4 (3 3 3 3)

# Based on this we can conclude that, if freq is 1 we can simply return -1, else, the number of moves required are represented by ceil(count / 3).

# Therefore, we first need to store the frequencies of each unique element, and then for each unique element, we can add the moves derived by the formula ceil(count / 3). If frequency of any element is equal to 1 --> return -1.

# Time Complexity: O(n)
# Space Complexity: O(n)
