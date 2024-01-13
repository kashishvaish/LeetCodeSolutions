class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        freq = [0]*26
        for i in range(len(s)):
            freq[ord(s[i])-97] += 1
            freq[ord(t[i])-97] -= 1
        result = 0
        for i in range(26):
            if freq[i] > 0: result += freq[i]
        return result

# Approach:
# To make the strings anagrams, we do not need to consider thr instances if characters that are present in both the strings. Therefore, the problem comes down to counting the number of characters that are different in both strings.
# To do this, we can store the difference of frequencies of each character in an array. The result will be either of the sum of all positive differences or the sum of all negative differences.

# Time Complexity: O(n)
# Space Complexity: O(1)
