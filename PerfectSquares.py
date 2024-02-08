class Solution:
    def numSquares(self, n: int) -> int:
        # Time Complexity: O(n x sqrt(n))
        # Space Complexity: O(n)
        dp = [0]*(n+1)
        for i in range(1, n+1):
            if int(i**0.5) * int(i**0.5) == i:
                dp[i] = 1
            else:
                k = 1
                while k*k <= i:
                    if dp[i] == 0:
                        dp[i] = dp[i - k*k] + 1
                    else:
                        dp[i] = min(dp[i], dp[i - k*k] + 1)
                    k += 1
        return dp[n]

# Dynamic Programming
# Use an array dp of size n+1 to keep track of the minimum number of perfect squares that sum up to number.
# dp[i] = minimum number of perfect squares that sum up to i

# Time Complexity: O(n x sqrt(n))
# Space Complexity: O(n)
