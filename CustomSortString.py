class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Time Complexity: O(m+n)
        # Space Complexity: O(n)
        freqs = {}
        result = ""
        for ch in s:
            freqs[ch] = freqs.get(ch, 0) + 1
        for ch in order:
            if freqs.get(ch, 0):
                result += ch*freqs[ch]
                freqs[ch] = 0
        for ch in freqs:
            if freqs[ch]: result += ch*freqs[ch]
        return result

# Approach:
# Begin by initializing an empty dictionary freqs to store the frequency of each character in the string s.
# Iterate through each character ch in the string s. For each character, update its frequency in the freqs dictionary.
# Initialize an empty string result to store the custom-sorted string.
# Iterate through each character ch in the order string. For each character, check if it exists in the freqs dictionary. If it does, append ch to the result string freqs[ch] times and set the frequency of ch to 0 in the freqs dictionary.
# Iterate through each remaining character ch in the freqs dictionary. For each character with a non-zero frequency, append ch to the result string freqs[ch] times.
# Finally, return the result string, which represents the custom-sorted string based on the given order.
    
# Time Complexity: O(m+n)
# Space Complexity: O(n)
