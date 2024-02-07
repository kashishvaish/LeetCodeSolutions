class Solution:
    def frequencySort(self, s: str) -> str:
        # Time Complexity: O(nlogn)
        # Space Complexity: O(n)
        d = {}
        for ch in s: d[ch] = d.get(ch, 0) + 1
        sorted_freqs = sorted(d.items(), key = lambda x: x[1], reverse = True)
        res = ""
        for ch, freq in sorted_freqs: res += ch*freq
        return res

# Approach:
# Store the frequency of each character in a hashmap.
# Sort the frequencies in descending order.
# Then construct the sorted string based on character frequencies.

# Time Complexity: O(nlogn)
# Space Complexity: O(n)
