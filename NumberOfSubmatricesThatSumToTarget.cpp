class Solution {
public:
    int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {
        // Time Complexity: O(m x n^2)
        // Space Complexity: O(mn)
        int M = 1000000000 + 7;
        int m = matrix.size();
        int n = matrix[0].size();
        int result = 0;
        for(int x = 0; x < m; x++) {
            for(int y = 1; y < n; y++) {
                matrix[x][y] += matrix[x][y-1];
            }
        }
        for(int c1 = 0; c1 < n; c1++) {
            for(int c2 = c1; c2 < n; c2++) {
                int sum = 0;
                unordered_map<int, int> map;
                map[0] = 1;
                for(int r = 0; r < m; r++) {
                    sum += matrix[r][c2] - (c1 > 0 ? matrix[r][c1-1] : 0);
                    result = (result + map[sum - target]) % M;
                    map[sum]++;
                }
            }
        }
        return result;
    }
};

// Naive Approach:
// Use nested loops to iterate through all possible submatrices. For each submatrix, calculate the sum of elements within the submatrix and increment the result if the sum matches the target.

// Code:
// class Solution {
// public:
//     int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {
//         // Time Complexity: O(m^3 x n^3)
//         // Space Complexity: O(1)
//         int M = 1000000000 + 7;
//         int m = matrix.size();
//         int n = matrix[0].size();
//         int result = 0;
//         for(int x1 = 0; x1 < m; x1++) {
//             for(int y1 = 0; y1 < n; y1++) {
//                 for(int x2 = x1; x2 < m; x2++) {
//                     for(int y2 = y1; y2 < n; y2++) {
//                         int sum = 0;
//                         for(int x = x1; x <= x2; x++) {
//                             for(int y = y1; y <= y2; y++) {
//                                 sum += matrix[x][y];
//                             }
//                         }
//                         if(sum == target) result = (result + 1) % M;
//                     }
//                 }
//             }
//         }
//         return result;
//     }
// };

// Time Complexity: O(m^3 x n^3)
// Space Complexity: O(1)



// Dynamic Programming:
// Use a 2D array dp to store the cumulative sums of submatrices, reducing the time complexity for sum calculations.

// Code:
// class Solution {
// public:
//     int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {
//         // Time Complexity: O(m^2 x n^2)
//         // Space Complexity: O(mn)
//         int M = 1000000000 + 7;
//         int m = matrix.size();
//         int n = matrix[0].size();
//         int result = 0;
//         for(int x1 = 0; x1 < m; x1++) {
//             for(int y1 = 0; y1 < n; y1++) {
//                 int dp[m][n];
//                 for(int x2 = x1; x2 < m; x2++) {
//                     for(int y2 = y1; y2 < n; y2++) {
//                         if(x1 == x2 && y1 == y2) dp[x2][y2] = matrix[x2][y2];
//                         else if(x1 == x2) dp[x2][y2] = dp[x2][y2-1] + matrix[x2][y2];
//                         else if(y1 == y2) dp[x2][y2] = dp[x2-1][y2] + matrix[x2][y2];
//                         else dp[x2][y2] = dp[x2][y2-1] + dp[x2-1][y2] - dp[x2-1][y2-1] + matrix[x2][y2];
//                         if(dp[x2][y2] == target) result = (result + 1) % M;
//                     }
//                 }
//             }
//         }
//         return result;
//     }
// };

// Time Complexity: O(m^2 x n^2)
// Space Complexity: O(mn)



// Prefix Sum:
// Iterate through each row and precompute the cumulative sum for each element in that row.
// Then, for each pair of columns, scan through rows to compute submatrix sums, eliminating the need for nested loops over each element. The map keeps track of encountered sums, making it easy to identify submatrices with the target sum.

// Code:
// class Solution {
// public:
//     int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {
//         // Time Complexity: O(m x n^2)
//         // Space Complexity: O(mn)
//         int M = 1000000000 + 7;
//         int m = matrix.size();
//         int n = matrix[0].size();
//         int result = 0;
//         for(int x = 0; x < m; x++) {
//             for(int y = 1; y < n; y++) {
//                 matrix[x][y] += matrix[x][y-1];
//             }
//         }
//         for(int c1 = 0; c1 < n; c1++) {
//             for(int c2 = c1; c2 < n; c2++) {
//                 int sum = 0;
//                 unordered_map<int, int> map;
//                 map[0] = 1;
//                 for(int r = 0; r < m; r++) {
//                     sum += matrix[r][c2] - (c1 > 0 ? matrix[r][c1-1] : 0);
//                     result = (result + map[sum - target]) % M;
//                     map[sum]++;
//                 }
//             }
//         }
//         return result;
//     }
// };

// Time Complexity: O(m x n^2)
// Space Complexity: O(mn)
