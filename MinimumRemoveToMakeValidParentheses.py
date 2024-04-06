class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        n = len(s)
        openIndex = []
        res = []
        curr = 0
        c = 0
        for i in range(n):
            if s[i] == "(":
                res.append(s[i])
                curr += 1
                openIndex.append(c)
                c += 1
            elif s[i] == ")":
                if curr == 0:
                    continue
                curr -= 1
                res.append(s[i])
                c += 1
            else:
                res.append(s[i])
                c += 1
        if curr > 0:
            for j in range(len(openIndex)-1, len(openIndex)-1-curr, -1):
                res[openIndex[j]] = ""
        return "".join(res)
    
# Approach:
# Initialize an empty list called openIndex to keep track of the indices of unmatched opening parentheses.
# Initialize an empty list called res to store the characters of the resulting string.
# Initialize two variables curr and c to keep track of the current count of unmatched opening parentheses and the current index in the resulting string, respectively.
# Iterate through each character in the input string s.
# For each character s[i]:
# a. If s[i] is an opening parenthesis "(", append it to res, increase curr by 1, append its index to openIndex, and increment c.
# b. If s[i] is a closing parenthesis ")", check if there are unmatched opening parentheses. If so, append ")" to res, decrease curr by 1, and increment c.
# c. Otherwise, if s[i] is neither an opening nor a closing parenthesis, append it to res and increment c.
# If there are still unmatched opening parentheses (curr > 0), iterate through the indices in openIndex corresponding to the unmatched opening parentheses and remove them from res.
# Return the resulting string obtained by joining the characters in res.

# Time Complexity: O(n)
# Space Complexity: O(n)
