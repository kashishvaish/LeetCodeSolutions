class Solution:
    def myAtoi(self, s: str) -> int:
        # Time: O(n)
        # Space: O(1)
        s = s.lstrip()
        if not s:
            return 0
        sign = 1
        if s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        num = 0
        i = 0
        while i < len(s) and s[i].isdigit():
            num = num*10 + int(s[i])
            i += 1
        num *= sign
        if num < -2**31:
            return -2**31
        elif num > 2**31-1:
            return 2**31 - 1
        return num
    
# Approach:

# 1. Remove leading whitespaces
# 2. if string is empty --> return 0
# 3. if first character is "-" --> set sign to -1 --> else, set sign to 1
# 4. for remaining characters till not digit is not found --> add digits to number
# 5. check for range
# 6. return number

# Time: O(n)
# Space: O(1)
