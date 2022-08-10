class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Time: O(log(n))
        # Space: O(1)
        copy = x
        rev = 0
        while copy > 0:
            rev = rev*10 + copy%10
            copy //= 10
        return x == rev
      
# Approach:

# Reverse the number --> compare
# Time: O(log(n))
# Space: O(1)
