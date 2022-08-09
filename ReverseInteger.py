class Solution:
    def reverse(self, x: int) -> int:
        # Time: O(log(n))
        # Space: O(1)
        sign = -1 if x < 0 else 1
        x = -x if x < 0 else x
        rev = 0
        while x:
            d = x % 10
            rev = rev*10 + d
            if rev > 2**31:
                return 0
            x //= 10
        return rev*sign
        
# Approach:

# Reverse the number one digit at a time --> check overflow on adding each digit --> return reverse if no overflow --> else return 0

# Time: O(log(n))
# Space: O(1)
