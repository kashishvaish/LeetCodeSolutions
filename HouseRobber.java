class Solution {
    public int rob(int[] nums) {
        // Time Complexity: O(n)
        // Space Complexity: O(1)
        int n = nums.length;
        if(n == 1) return nums[0];
        if(n == 2) return Math.max(nums[0], nums[1]);
        int a = nums[0];
        int b = nums[1];
        int c = nums[0]+nums[2];
        for(int i = 3; i < n; i++) {
            int curr = Math.max(a, b) + nums[i];
            a = b;
            b = c;
            c = curr;
        }
        return Math.max(b, c);
    }
}

// Dynamic Programming
// Use an array dp, such that dp[i] stores the maximum amount of money that can be robbed including the ith house 
// Maximum amount of money that can be robbed including the ith house will be equal to nums[i] + maximum of amount till i-2 and amount till i-3.
// dp[i] = max(dp[i-2], dp[i-3]) + nums[i]

// Code:
// class Solution {
//     public int rob(int[] nums) {
//         // Time Complexity: O(n)
//         // Space Complexity: O(n)
//         int n = nums.length;
//         if(n == 1) return nums[0];
//         if(n == 2) return Math.max(nums[0], nums[1]);
//         int[] dp = new int[n];
//         dp[0] = nums[0];
//         dp[1] = nums[1];
//         dp[2] = nums[0]+nums[2];
//         for(int i = 3; i < n; i++) {
//             dp[i] = Math.max(dp[i-2], dp[i-3]) + nums[i];
//         }
//         return Math.max(dp[n-1], dp[n-2]);
//     }
// }

// Time Complexity: O(n)
// Space Complexity: O(n)


// Space Optimization:
// We only need to track the values of dp[i-1], dp[i-2], and dp[i-3]. We can do this using variables instead.

// Code:
// class Solution {
//     public int rob(int[] nums) {
//         // Time Complexity: O(n)
//         // Space Complexity: O(1)
//         int n = nums.length;
//         if(n == 1) return nums[0];
//         if(n == 2) return Math.max(nums[0], nums[1]);
//         int a = nums[0];
//         int b = nums[1];
//         int c = nums[0]+nums[2];
//         for(int i = 3; i < n; i++) {
//             int curr = Math.max(a, b) + nums[i];
//             a = b;
//             b = c;
//             c = curr;
//         }
//         return Math.max(b, c);
//     }
// }

// Time Complexity: O(n)
// Space Complexity: O(1)
