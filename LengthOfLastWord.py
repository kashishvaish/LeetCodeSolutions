class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
    
# Approach:
# The split() method is used to split the string s into a list of words based on whitespace.
# s.split()[-1] is used to access the last element (which represents the last word) of the resulting list.
# len(s.split()[-1]) calculates the length of the last word.

# Time Complexity: O(n)
# Space Complexity: O(n)
