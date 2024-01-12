class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        n = len(s)
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        c1 = 0
        c2 = 0
        for i in range(n//2):
            if s[i] in vowels: c1+=1
        for i in range(n//2, n):
            if s[i] in vowels: c2+=1
        if c1 == c2: return True
        return False

# Approach:
# Count the number of vowels in each half. --> If equal, return True. Else, return False.

# Time Complexity: O(n)
# Space Complexity: O(1)
