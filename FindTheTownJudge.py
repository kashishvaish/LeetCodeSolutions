class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Time Complexity: O(n + m)
        # Space Complexity: O(n)
        d = {i:[0,0] for i in range(1, n+1)}
        for u, v in trust:
            d[u][0] += 1
            d[v][1] += 1
        for i in d:
            if d[i][0] == 0 and d[i][1] == n-1: return i
        return -1

# Approach:
# Create a dictionary d where each key represents a person labeled from 1 to n, and each value is initialized as a list [0, 0].
# The first element of the list tracks the count of people the person trusts, while the second element tracks the count of people who trust the person.
# Iterate through each trust relationship [u, v] in the trust array.
# For each trust relationship, increment the first element of the value corresponding to the trusting person u, and increment the second element of the value corresponding to the trusted person v.
# Iterate through each person in the town represented by the keys in the dictionary d.
# Check if the person trusts nobody (d[i][0] == 0) and if everybody (except themselves) trusts the person (d[i][1] == n-1).
# If both conditions are met for a person, return that person's label as the town judge.
# If no such person is found after iterating through all people, return -1 to indicate that there is no town judge.

# Time Complexity: O(n + m)
# Space Complexity: O(n)
