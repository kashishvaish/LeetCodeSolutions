class Solution:
    def maxDepth(self, s: str) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        res = 0
        curr = 0
        for ch in s:
            if ch == "(":
                curr += 1
                res = max(res, curr)
            elif ch == ")":
                curr -= 1
        return res
    
# Approach:
# Initialize a variable res to 0. This will store the maximum nesting depth so far.
# Initialize a variable curr to 0. This will store the current open brackets count.
# Iterate over the characters in the string s, for each character ch:
#     If ch is equal to (, increment the counter curr, and update res as the max of res and curr.
#     If ch is equal to ), decrement the counter curr.
# Return res.

# Time Complexity: O(n)
# Space Complexity: O(1)
