class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Time Complexity: O(m+n)
        # Space Complexity: O(m+n)
        if not s or not t: return ""
        d = {}
        for ch in t: d[ch] = d.get(ch, 0) + 1
        req = len(d)
        left = 0
        right = 0
        formed = 0
        count = {}
        ans = [-1, 0, 0]
        while right < len(s):
            ch = s[right]
            count[ch] = count.get(ch, 0) + 1
            if ch in d and count[ch] == d[ch]: formed += 1
            while left <= right and formed == req:
                ch = s[left]
                if ans[0] == -1 or right - left + 1 < ans[0]:
                    ans[0] = right - left + 1
                    ans[1] = left
                    ans[2] = right
                count[ch] -= 1
                if ch in d and count[ch] < d[ch]: formed -= 1
                left += 1
            right += 1
        return "" if ans[0] == -1 else s[ans[1]: ans[2] + 1]

# Approach:
# Use the sliding window technique where two pointers represent the left and right ends of the current window.
# d is used to count the occurrences of characters in string t.
# count keeps track of the characters within the current window.
# Move the right pointer to expand the window.
# Check if the characters in the current window satisfy the required counts from t.
# If satisfied, increment the count of characters satisfying the required counts.
# Move the left pointer to shrink the window.
# Update the minimum window size if a smaller valid window is found.
# Continue this process until a smaller valid window is not possible.
# Repeat until the right pointer reaches the end of the string.

# Time Complexity: O(m+n)
# Space Complexity: O(m+n)
