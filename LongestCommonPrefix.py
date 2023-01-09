class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Vertical Scanning
        # Time: O(n*k) where k is the length of lcp
        # Space: O(1)
        
        if not strs: return ""
        index = -1
        curr = None
        status = True
        while status:
            index += 1
            for i in range(len(strs)):
                if index >= len(strs[i]):
                    status = False
                    break;
                elif i == 0:
                    curr = strs[i][index]
                elif strs[i][index] != curr:
                    status = False
                    break;  
        return strs[0][:index]    

#Longest Common Prefix

# Method 1: Horizontal Scanning
# take the first string as lcp
# for remaining strings keep eliminating the uncommon part from lcp
# return lcp

# Example:
# ["flower","flow","flight"]
# lcp = "flower"
# compare with flow --> lcp = "flow"
# compare with flight --> lcp = "fl"
# rerturn lcp = "fl"

# Time: O(m*n)
# Space: O(1)


# Method 2: Vertical Scanning
# compare characters index by index
# return substring before the first mismatch occurs

# ["flower","flow","flight"]
# index = 0 --> "f" --> match
# index = 1 --> "l" --> match
# index = 2 --> mismatch
# return substring till index 1 --> "fl"

# Time: O(n*k) where k is the length of lcp
# Space: O(1)
