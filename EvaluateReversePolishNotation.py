class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        stack = []
        for ch in tokens:
            if ch in "+-*/":
                op2 = stack.pop()
                op1 = stack.pop()
                if ch == "+":
                    stack.append(op1 + op2)
                elif ch == "-":
                    stack.append(op1 - op2)
                elif ch == "*":
                    stack.append(op1 * op2)
                else:
                    stack.append(int(op1 / op2))
            else:
                stack.append(int(ch))
        return stack.pop()

# Approach:
# Iterate through the list of tokens from left to right.
# If the current token is a number, it is pushed onto the stack.
# If the current token is an operator (+, -, *, /), the top two elements from the stack (operands) are popped and the operation is performed, and the result is pushed back onto the stack.
# The process continues until all tokens are processed, and the final result is the only element remaining in the stack.

# Time Complexity: O(n)
# Space Complexity: O(n)
