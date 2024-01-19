class Solution {
    public int minFallingPathSum(int[][] matrix) {
        // Time Complexity: O(n^2)
        // Space Complexity: O(n)
        int n = matrix.length;
        int[] prev = new int[n];
        int[] curr = new int[n];
        for(int i = 0; i < n; i++) {
            prev[i] = matrix[0][i];
        }
        for(int row = 1; row < n; row++) {
            for(int col = 0; col < n; col++) {
                int minimum = prev[col];
                if(col-1 >= 0) {
                    minimum = Math.min(minimum, prev[col-1]);
                }
                if(col+1 < n) {
                    minimum = Math.min(minimum, prev[col+1]);
                }
                curr[col] = minimum + matrix[row][col];
            }
            for(int i = 0; i < n; i++) {
                prev[i] = curr[i];
            }
        }
        int result = prev[0];
        for(int i = 1; i < n; i++) {
            result = Math.min(prev[i], result);
        }
        return result;
    }
}

// Dynamic Programming:
// Create a table dp of size n x n.
// dp[i][j] should store the minimum sum of any falling path ending at dp[i][j].

// Code:
// class Solution {
//     public int minFallingPathSum(int[][] matrix) {
//         // Time Complexity: O(n^2)
//         // Space Complexity: O(n^2)
//         int n = matrix.length;
//         int[][] dp = new int[n][n];
//         for(int i = 0; i < n; i++) {
//             dp[0][i] = matrix[0][i];
//         }
//         for(int row = 1; row < n; row++) {
//             for(int col = 0; col < n; col++) {
//                 int minimum = dp[row-1][col];
//                 if(col-1 >= 0) {
//                     minimum = Math.min(minimum, dp[row-1][col-1]);
//                 }
//                 if(col+1 < n) {
//                     minimum = Math.min(minimum, dp[row-1][col+1]);
//                 }
//                 dp[row][col] = minimum + matrix[row][col];
//             }
//         }
//         int result = dp[n-1][0];
//         for(int i = 1; i < n; i++) {
//             result = Math.min(dp[n-1][i], result);
//         }
//         return result;
//     }
// }

// Time Complexity: O(n^2)
// Space Complexity: O(n^2)


// Space Optimization:
// We know that we only need values from previous row to get the current row, so we can just store the previous and current rows.

// Code:
// class Solution {
//     public int minFallingPathSum(int[][] matrix) {
//         // Time Complexity: O(n^2)
//         // Space Complexity: O(n)
//         int n = matrix.length;
//         int[] prev = new int[n];
//         int[] curr = new int[n];
//         for(int i = 0; i < n; i++) {
//             prev[i] = matrix[0][i];
//         }
//         for(int row = 1; row < n; row++) {
//             for(int col = 0; col < n; col++) {
//                 int minimum = prev[col];
//                 if(col-1 >= 0) {
//                     minimum = Math.min(minimum, prev[col-1]);
//                 }
//                 if(col+1 < n) {
//                     minimum = Math.min(minimum, prev[col+1]);
//                 }
//                 curr[col] = minimum + matrix[row][col];
//             }
//             for(int i = 0; i < n; i++) {
//                 prev[i] = curr[i];
//             }
//         }
//         int result = prev[0];
//         for(int i = 1; i < n; i++) {
//             result = Math.min(prev[i], result);
//         }
//         return result;
//     }
// }

// Time Complexity: O(n^2)
// Space Complexity: O(n)
