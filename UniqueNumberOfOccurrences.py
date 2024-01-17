class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        freq = {}
        for i in arr:
            freq[i] = freq.get(i, 0) + 1
        uniques = set()
        for i in freq.values():
            if i in uniques:
                return False
            uniques.add(i)
        return True

# Approach:
# Store the elements and their corresponding frequencies in a hashmap.
# Iterate over the hashmap to check for repeating values.

# Time Complexity: O(n)
# Space Complexity: O(n)
