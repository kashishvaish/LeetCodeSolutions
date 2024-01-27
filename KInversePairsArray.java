class Solution {
    public int kInversePairs(int n, int k) {
        // Time Complexity: O(n x n x k)
        // Space Complexity: O(n x k)
        int M = 1000000000 + 7;
        int dp[][] = new int[n+1][k+1];
        dp[0][0] = 1;
        for(int i = 1; i <= n; i++) {
            for(int j = 0; j <= k; j++) {
                for(int x = 0; x <= Math.min(j, i-1); x++) {
                    if(j-x >= 0) dp[i][j] = (dp[i][j] + dp[i-1][j-x]) % M;
                }
            }
        }
        return dp[n][k];
    }
}



// Brute Force
// Generate all possible permutations.
// Count the number of inverse pairs in each permutation.
// Return the count of permutations with k inverse pairs.

// Time Complexity: O(n^2 x n!)
// Space Complexity: O(n)



// Optimized Recursion:
// Since all numbers are unique, the numbers remaining to be inserted in permuation does not matter, all that matters is the number of elements remaining.

// Time Complexity: O(n x n!)
// Space Complexity: O(n)



// Memoization
// Create a dp array of size n x k to avoid redundant computations.

// Time Complexity: O(n x n x k)
// Space Complexity: O(n x k)



// Dynamic Programming
// We create a 2D array dp, where dp[i][j] represents the number of arrays with i elements and j inverse pairs.

// Time Complexity: O(n x n x k)
// Space Complexity: O(n x k)
