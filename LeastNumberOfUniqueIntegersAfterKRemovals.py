class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # Time Complexity: O(nlogn)
        # Space Complexity: O(n)
        freq = {}
        for num in arr: freq[num] = freq.get(num, 0) + 1
        freqs = sorted(freq.values())
        total = len(freqs)
        for freq in freqs:
            if k >= freq:
                k -= freq
                total -= 1
            else:
                break
        return total
    
# Approach:
# Use a hashmap to calculate the frequencies of elements in arr.
# Store the frequencies in an array and sort them in ascending order.
# Iterate over the sorted array to remove at most k elements, keeping track of the elements completely removed.
# Return the remaining number of unique elements.

# Time Complexity: O(nlogn)
# Space Complexity: O(n)
