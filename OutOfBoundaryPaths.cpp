class Solution {
public:
    int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        // Time Complexity: O(m x n x maxMove)
        // Space Complexity: O(m x n)
        int M = 1000000000 + 7;
        int result = 0;
        int dp[m][n];
        memset(dp, 0, sizeof(dp));
        dp[startRow][startColumn] = 1;
        for(int i = 1; i <= maxMove; i++) {
            int temp[m][n];
            for(int row = 0; row < m; row++) {
                for(int col = 0; col < n; col++) {
                    if(row == 0) result = (result + dp[row][col]) % M;
                    if(col == 0) result = (result + dp[row][col]) % M;
                    if(row == m-1) result = (result + dp[row][col]) % M;
                    if(col == n-1) result = (result + dp[row][col]) % M;
                    temp[row][col] = 0;
                    if(row > 0) temp[row][col] = (temp[row][col] + dp[row-1][col]) % M;
                    if(col > 0) temp[row][col] = (temp[row][col] + dp[row][col-1]) % M;
                    if(row+1 < m) temp[row][col] = (temp[row][col] + dp[row+1][col]) % M;
                    if(col+1 < n) temp[row][col] = (temp[row][col] + dp[row][col+1]) % M;
                }
            }
            for(int i = 0; i < m; i++) {
                for(int j = 0; j < n; j++) {
                    dp[i][j] = temp[i][j];
                }
            }
        }
        return result;
    }
};

// Naive Approach
// The problem can be approached using a recursive depth-first search (DFS) strategy.
// The idea is to explore all possible moves of the ball in the grid and count the paths that lead to moving the ball out of the grid boundary within the given maximum number of moves.

// Time Complexity: O(4^maxMove)
// Space Complexity: O(maxMove)



// Recursion with Memoization
// The idea is to use a 3D array dp to store intermediate results, avoiding redundant computations during recursive calls.
// This helps in reducing the time complexity compared to the purely recursive solution.

// Time Complexity: O(m x n x maxMove)
// Space Complexity: O(m x n x maxMove)



// Dynamic Programming
// The approach involves maintaining a 2D array dp of size m x n to represent the number of ways the ball can reach each cell in the grid after a certain number of moves.
// The result is accumulated by considering the edges of the grid in each iteration.

// Example: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
//  O _
//  _ _

// move = 0
// 1 0
// 0 0

// move = 1
// 1 1
// 1 0

// move = 2
// (0, 0) --> 1 ball and can go out in two ways = 2
// (0, 1) --> 1 ball and can go out in two ways = 2
// (1, 0) --> 1 ball and can go out in two ways = 2
// (0, 0) --> 0 ball and can go out in two ways = 0

// Ways: 2 + 2 + 2 + 0 = 6

// Time Complexity: O(m x n x maxMove)
// Space Complexity: O(m x n)
