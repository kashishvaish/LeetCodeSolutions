class Solution:
    def makeGood(self, s: str) -> str:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        stack = []
        for ch in s:
            if not stack: stack.append(ch)
            elif stack[-1] != ch and stack[-1].lower() == ch.lower(): stack.pop()
            else: stack.append(ch)
        return "".join(stack)

# Approach:
# Initialize an empty stack to store characters.
# Iterate through each character in the input string s.
# For each character ch:
# If the stack is empty, push ch onto the stack.
# If the stack is not empty and the top character of the stack is different from ch, but they have the same letter (ignoring case), pop the top character from the stack (as it forms a pair with ch).
# Otherwise, push ch onto the stack.
# Finally, join the remaining characters in the stack to form the resulting string without adjacent pairs.

# Time Complexity: O(n)
# Space Complexity: O(n)
