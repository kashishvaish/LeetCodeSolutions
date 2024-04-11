class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        stack = []
        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        while k:
            stack.pop()
            k -= 1
        result = "".join(stack).lstrip("0")
        if result: return result
        else: return "0"
        
# Approach: Greedy + Stack
# Initialize an empty stack.
# Traverse each digit of num.
# For each digit, while the stack is not empty and k is greater than zero, check if the current digit is smaller than the top of the stack. If so, pop from the stack (remove the top digit) and decrement k.
# Push the current digit onto the stack.
# After processing all digits, handle remaining k (if any) by popping from the stack.
# Construct the resulting number from the stack and remove any leading zeros.
# Return the smallest possible number as a string.

# Time Complexity: O(n)
# Space Complexity: O(n)
