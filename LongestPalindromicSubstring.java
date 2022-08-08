class Solution {
    public String longestPalindrome(String s) {
        // Time: O(n^2)
        // Space: O(n^2)
        int n = s.length();
        if(n == 0) {
            return "";
        }
        int maxLen = 1;
        int start = 0;
        boolean dp[][] = new boolean[n][n];
        for(int i = 0; i < n; i++) {
            dp[i][i] = true;
            if(i < n-1) {
                if(s.charAt(i) == s.charAt(i+1)) {
                    dp[i][i+1] = true;
                    if(maxLen < 2) {
                        maxLen = 2;
                        start = i;
                    }
                }
            }
        }
        for(int d = 2; d < n; d++) {
            for(int i = 0; i < n-d; i++) {
                dp[i][i+d] = dp[i+1][i+d-1] && s.charAt(i) == s.charAt(i+d);
                if(dp[i][i+d] && maxLen < d+1) {
                    maxLen = d+1;
                    start = i;
                }
            }
        }
        return s.substring(start, start+maxLen);
    }
}

// Approach:

// 1. Brute Force Approach

// For every substring --> check whether it is palindrome or not --> return the max length palindromic string
// Time: O(n^3)
// Space: O(1)

// 2. Dynamic Programming

// Intuition: 
// String with length 1 --> always palindrome
// String with length 2 --> palindrome if both values are equal
// Else --> palindrome if (substring excluding first and last character is palindrome) and (first value == last value)
// Time: O(n^2)
// Space: O(n^2)
