class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # Time Complexity: O(nlogn)
        # Space Complexity: O(n)
        n = len(tokens)
        low = 0
        high = n-1
        score = 0
        tokens.sort()
        while low <= high:
            if power >= tokens[low]:
                power -= tokens[low]
                score += 1
                low += 1
            elif low < high and score > 0:
                score -= 1
                power += tokens[high]
                high -= 1
            else:
                break
        return score
    
# Approach: Two Pointer
# Initialize a pointer low to 0 and high to tokens.length - 1.
# Initialize a variable score to 0.
# Sort tokens in ascending order.
# While low is less than or equal to high:
# If power is greater than or equal to tokens[low], we have enough power to play a token face-up. We increment score by 1, reduce power by tokens[low], and increase low by 1.
# Else if score is greater than 0, and low is less than high, we play a token face-down. We decrease score by 1, increase our power by tokens[high], and decrease high by 1.
# Otherwise, we don't have enough power to play a token face-up, and we either don't have enough score to play a token face-down or not enough tokens remain to make it worth playing a token face-down, so we break the loop.
# Finally, return score.

# Time Complexity: O(nlogn) for sorting
# Space Complexity: O(n) for sorting
