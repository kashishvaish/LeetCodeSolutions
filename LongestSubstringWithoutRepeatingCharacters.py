class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time: O(n)
        # Space: O(n)
        start = 0
        maxLen = 0
        hashMap = {}
        for i, ch in enumerate(s):
            if ch in hashMap and hashMap[ch] >= start:
                start = hashMap[ch]+1
            maxLen = max(maxLen, i-start+1)
            hashMap[ch] = i
        return maxLen
            
# Approach

# 1. Brute Force Approach

# For each possible substring --> check whether it has any repeating character --> return length of the longest such substring

# Time: O(n^4)
# Space: O(1)

# 2. Optimized Brute Force

# For each possible substring --> check whether it has any repeating character using hashSet --> return length of the longest such substring

# Time: O(n^2)
# Space: O(n)

# 3. Sliding Window

# The idea is to store, characters along with the index where they last occured in a hashMap as key and value respectively.
# Use variable window size sliding window --> initially setting the left end at index 0 --> if a character is seen which is already in the window --> decrease the window size by shifting left pointer to place where the character occured last + 1 --> keep track of the maximum size of window.

# Time: O(n)
# Space: O(n)
