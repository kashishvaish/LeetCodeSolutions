class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        // Time Complexity: O(mxn)
        // Space Complexity: O(mxn)
        int m = text1.length();
        int n = text2.length();
        int[][] dp = new int[m+1][n+1];
        for(int i = 1; i <= m; i++) {
            for(int j = 1; j <= n; j++) {
                if(text1.charAt(i-1) == text2.charAt(j-1)) {
                    dp[i][j] = dp[i-1][j-1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }
        return dp[m][n];
    }
}

// Dynamic Programming:
// The intuition behind the dynamic programming approach is to use a 2D array dp to store the lengths of LCS for various prefixes of the input strings.
// By comparing characters at each position, the algorithm fills up the dp array and computes the length of the LCS iteratively.

// Example: text1 = "abcde", text2 = "ace"
//     a c e
//   0 0 0 0
// a 0 1 1 1
// b 0 1 1 1
// c 0 1 2 2
// d 0 1 2 2
// e 0 1 2 3

// Time Complexity: O(mxn)
// Space Complexity: O(mxn)
