class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        m = len(word1)
        n = len(word2)
        if m != n: return False
        freq1 = [0]*26
        freq2 = [0]*26
        for i in range(n):
            freq1[ord(word1[i])-97] += 1
            freq2[ord(word2[i])-97] += 1
        for i in range(26):
            if (freq1[i] == 0) != (freq2[i] == 0):
                return False
        return sorted(freq1) == sorted(freq2) 

# Approach
# If lengths are different, return False.
# Store the frequency of each letter in both strings.
# If a character is present in one word and not in another, return False.
# Two strings can be made close, if the values of frequencies are same, irrespective of the order.
# Sort the frequencies and compare them, if the sorted frequencies are equal --> return True, else --> return False.

# Time Complexity: O(n)
# Space Complexity: O(1)
