class Solution:
    def climbStairs(self, n: int) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        secondlast = 1
        last = 1
        new = 1
        for i in range(2, n+1):
            new = last+secondlast
            secondlast = last
            last = new
        return new
        

# Approach - Dynamic Programming:
# Total ways to reach nth step = Total ways to reach n-1th step + Total ways to reach n-2th step

# Code:
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         # Time Complexity: O(n)
#         # Space Complexity: O(n)
#         dp = [0]*(n+1)
#         dp[0] = 1
#         dp[1] = 1
#         for i in range(2, n+1):
#             dp[i] = dp[i-1]+dp[i-2]
#         return dp[n]

# Time Complexity: O(n)
# Space Complexity: O(n)


# Space Optimization
# As we are only concerned about last and second last values, we can track them only using variables.

# Code:
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         # Time Complexity: O(n)
#         # Space Complexity: O(1)
#         secondlast = 1
#         last = 1
#         new = 1
#         for i in range(2, n+1):
#             new = last+secondlast
#             secondlast = last
#             last = new
#         return new

# Time Complexity: O(n)
# Space Complexity: O(1)
