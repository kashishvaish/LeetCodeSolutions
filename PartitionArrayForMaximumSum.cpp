class Solution {
public:
    int maxSumAfterPartitioning(vector<int>& arr, int k) {
        // Time Complexity: O(nk)
        // Space Complexity: O(n)
        int n = arr.size();
        int dp[n+1];
        memset(dp, 0, sizeof(dp));
        for(int i = n-1; i >= 0; i--) {
            int currMax = 0;
            for(int j = i; j < min(n, i+k); j++) {
                currMax = max(currMax, arr[j]);
                dp[i] = max(dp[i], currMax * (j-i+1) + dp[j+1]);
            }
        }
        return dp[0];
    }
};

// Approach: Top-Down Dynamic Programming
// At each index, we decide the length of the subarray (from 1 to k) with that index as the starting point.
// Iterate over elements, maintaining the maximum value encountered (currMax).
// Assume each element in the subarray as the maximum value and calculate the sum.
// Recursively calculate the maximum sum for the remaining array after the subarray.
// Keep track of the maximum sum for each choice of subarray length.
// Memoize results to avoid redundant calculations.

// Code:
// class Solution {
// public:
//     int maxSumAfterPartitioning(vector<int>& arr, int k) {
//         // Time Complexity: O(nk)
//         // Space Complexity: O(n)
//         int n = arr.size();
//         int dp[n];
//         memset(dp, -1, sizeof(dp));
//         return util(0, n, arr, k, dp);
//     }

//     int util(int i, int n, vector<int>& arr, int k, int dp[]) {
//         if(i == n) return 0;
//         if(dp[i] != -1) return dp[i];
//         int currMax = 0;
//         int ans = 0;
//         for(int j = i; j < min(n, i+k); j++) {
//             currMax = max(currMax, arr[j]);
//             ans = max(ans, currMax * (j-i+1) + util(j+1, n, arr, k, dp));
//         }
//         dp[i] = ans;
//         return ans;
//     }
// };

// Time Complexity: O(nk)
// Space Complexity: O(n)


// Approach: Bottom-Up Dynamic Programming
// Traverse the array in reverse order.
// Calculate and update the optimal sum for each subarray starting from the current index.
// At each step, identify the maximum element within the current subarray,
// and for each possible subarray length, calculate the sum, considering the contribution of the current subarray and the optimal sum for the remaining array.

// Code:
// class Solution {
// public:
//     int maxSumAfterPartitioning(vector<int>& arr, int k) {
//         // Time Complexity: O(nk)
//         // Space Complexity: O(n)
//         int n = arr.size();
//         int dp[n+1];
//         memset(dp, 0, sizeof(dp));
//         for(int i = n-1; i >= 0; i--) {
//             int currMax = 0;
//             for(int j = i; j < min(n, i+k); j++) {
//                 currMax = max(currMax, arr[j]);
//                 dp[i] = max(dp[i], currMax * (j-i+1) + dp[j+1]);
//             }
//         }
//         return dp[0];
//     }
// };

// Time Complexity: O(nk)
// Space Complexity: O(n)
