class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Time: O(n)
        # Space: O(n)
        if numRows == 1:
            return s
        pattern = ["" for i in range(numRows)]
        curr = 0
        up = False
        for ch in s:
            pattern[curr] += ch
            if not up and curr == numRows-1:
                curr -= 1
                up = True
            elif not up:
                curr += 1
            elif up and curr == 0:
                curr += 1
                up = False
            elif up:
                curr -= 1
        return "".join(pattern)
    
# Approach:

# Traverse through the string --> append each character to the row it belongs to using current row index and direction (up / down) --> merge rows.

# Time: O(n)
# Space: O(n)
