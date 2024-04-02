class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        m = len(s)
        n = len(t)
        if m != n: return False
        d = {}
        chars = set()
        for i in range(n):
            if s[i] not in d:
                if t[i] in chars: return False
                d[s[i]] = t[i]
                chars.add(t[i])
            if d[s[i]] != t[i]: return False
        return True

# Approach:
# It first checks if the lengths of the two strings s and t are different. If they are not equal, the function returns False since strings of different lengths cannot be isomorphic.
# It initializes a dictionary d to store the mapping of characters from string s to string t, and a set chars to keep track of characters in t that have already been mapped.
# It iterates through the characters of both strings simultaneously using a single loop. For each character pair (s[i], t[i]):
# If the character s[i] is not already mapped in the dictionary d, it checks whether the corresponding character t[i] has already been mapped to a different character in s (i.e., if t[i] is present in the set chars). If t[i] is already in chars, it means that s[i] cannot be mapped to t[i] as it would violate the isomorphic condition. In this case, the function returns False. Otherwise, it adds the mapping s[i] -> t[i] to the dictionary d and adds t[i] to the set chars.
# If the character s[i] is already mapped in the dictionary d, it checks whether the existing mapping d[s[i]] is equal to t[i]. If they are not equal, it means that s[i] cannot be mapped to t[i] as it would violate the isomorphic condition. In this case, the function returns False.
# If the loop completes without returning False, it means that the strings s and t are isomorphic, and the function returns True.

# Time Complexity: O(n)
# Space Complexity: O(n)
