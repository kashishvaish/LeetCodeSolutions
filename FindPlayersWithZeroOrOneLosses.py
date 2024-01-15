class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # Time Complexity: O(nlogn)
        # Space Complexity: O(n)
        players = {}
        for m in matches:
            if m[0] not in players:
                players[m[0]] = 0
            if m[1] not in players:
                players[m[1]] = 0
            players[m[1]] += 1
        zero = []
        one = []
        for p in players:
            if players[p] == 0:
                zero.append(p)
            elif players[p] == 1:
                one.append(p)
        return [sorted(zero), sorted(one)]

# Approach
# Create a disctionary/hashmap to store the players and their number of losses.
# Store players with 0 and 1 losses in different lists.
# Sort them and return the answer.

# Time Complexity: O(nlogn)
# Space Complexity: O(n)
