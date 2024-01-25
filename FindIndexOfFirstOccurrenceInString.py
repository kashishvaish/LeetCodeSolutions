class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Time Complexity: O(mxn)
        # Space Complexity: O(1)
        m = len(needle)
        n = len(haystack)
        for i in range(n-m+1):
            for j in range(m):
                if haystack[i+j] != needle[j]:
                    break
            else:
                return i
        return -1

# Brute-force approach:
# Iterate through the haystack string and check for a potential match with the needle string at each position.
# If a match is found, return the starting index of the match; otherwise, return -1.

# Time Complexity: O(mxn)
# Space Complexity: O(1)
