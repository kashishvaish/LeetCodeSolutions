class Solution {
    public int climbStairs(int n) {
        // Time Complexity: O(n)
        // Space Complexity: O(1)
        int secondlast = 1;
        int last = 1;
        for(int i = 2; i <= n; i++) {
            int current = secondlast + last;
            secondlast = last;
            last = current;
        }
        return last;
    }
}

// Approach - Dynamic Programming:
// Total ways to reach nth step = Total ways to reach n-1th step + Total ways to reach n-2th step

// Code:
// class Solution {
//     public int climbStairs(int n) {
//         // Time Complexity: O(n)
//         // Space Complexity: O(n)
//         int[] dp = new int[n+1];
//         dp[0] = 1;
//         dp[1] = 1;
//         for(int i = 2; i <= n; i++) {
//             dp[i] = dp[i-1]+dp[i-2];
//         }
//         return dp[n];
//     }
// }

// Time Complexity: O(n)
// Space Complexity: O(n)


// Space Optimization
// As we are only concerned about last and second last values, we can track them only using variables.

// Code:
// class Solution {
//     public int climbStairs(int n) {
//         // Time Complexity: O(n)
//         // Space Complexity: O(1)
//         int secondlast = 1;
//         int last = 1;
//         for(int i = 2; i <= n; i++) {
//             int current = secondlast + last;
//             secondlast = last;
//             last = current;
//         }
//         return last;
//     }
// }

// Time Complexity: O(n)
// Space Complexity: O(1)
