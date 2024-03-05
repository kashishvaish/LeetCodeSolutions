class Solution:
    def minimumLength(self, s: str) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        n = len(s)
        start = 0
        end = n-1
        while start < end and s[start] == s[end]:
            ch = s[start]
            while start <= end and ch == s[start]:
                start += 1
            while  start < end and ch == s[end]:
                end -= 1
        return end-start+1

# Approach: Two Pointers
# Initialize two variables, start to 0 and end to length of s - 1. start points to the first index of s and end points to the last index.
# While start is less than end and the character at s[start] equals the character at s[end]:
# Initialize a character ch to s[start].
# While start is less than or equal to end and s[start] equals ch, increment start by 1 to delete a prefix character.
# While end is greater than start and s[end] equals ch, decrement end by 1 to delete a suffix character.
# After processing s, return end - start + 1, the number of remaining characters.

# Time Complexity: O(n)
# Space Complexity: O(1)
