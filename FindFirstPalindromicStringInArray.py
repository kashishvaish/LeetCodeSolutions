class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # Time Complexity: O(n x m)
        # Space Complexity: O(1)
        for word in words:
            start = 0
            end = len(word) - 1
            while start < end:
                if word[start] != word[end]: break
                start += 1
                end -= 1
            else:
                return word
        return ""

# Approach:
# For each string check if it is palindrome or not using two pointers approach.
# Return the first palindromic string.
    
# Time Complexity: O(n x m)
# Space Complexity: O(1)
