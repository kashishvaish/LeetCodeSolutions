class Solution {
    public int lengthOfLIS(int[] nums) {
        // Time Complexity: O(nlogn)
        // Space Complexity: O(n)
        int n = nums.length;
        if(n == 0) return 0;
        int[] result = new int[n];
        result[0] = nums[0];
        int length = 1;
        for(int i = 1; i < n; i++) {
            if(result[length-1] < nums[i]) {
                result[length] = nums[i];
                length++;
            }
            else {
                int left = 0;
                int right = length-1;
                while(left < right) {
                    int mid = (left+right)/2;
                    if(result[mid] >= nums[i]) {
                        right = mid;
                    } else {
                        left = mid+1;
                    }
                }
                result[right] = nums[i];
            }
        }
        return length;
    }
}



// Brute force
// Generate all the subsequences (Recursion, Power Set) --> Check for increasing trend --> Return the longest
// For each element we can either take it or not take it in the LIS --> this will be based on the previous element in LIS --> for this we need to store the index of previous element in LIS.
// Starting at index = 0 and previndex = -1
// 1. We can take item at index i if, previndex == -1 or nums[previndex] < nums[i]: in that case increment the length by 1 and make previndex = i
// 2. We can not take the item at index i: in that case length and pevious both will remain same.
// Base condition will be when i == n --> in that case length will be 0.

// Code:
// class Solution {
//     public int lengthOfLIS(int[] nums) {
//         // Time Complexity: O(2^n)
//         // Space Complexity: O(n) stack space
//         int n = nums.length;
//         return util(0, -1, n, nums);       
//     }

//     public int util(int curr, int prev, int n, int[] nums) {
//         if(curr == n) return 0;
//         int length = util(curr+1, prev, n, nums);
//         if(prev == -1 || nums[curr] > nums[prev]) {
//             length = Math.max(length, 1 + util(curr+1, curr, n, nums));
//         }
//         return length;
//     }
// }

// Time Complexity: O(2^n)
// Space Complexity: O(n) stack space



// Memoization:
// Create a table of size N x N+1, here, row indices represent current index and column indices store the prev index.
// Use this table to store values as we proceed with the recursive approach.
// This will reduce the time complexity to O(n^2).

// Code:
// class Solution {
//     public int lengthOfLIS(int[] nums) {
//         // Time Complexity: O(n^2)
//         // Space Complexity: O(n^2)
//         int n = nums.length;
//         int[][] dp = new int[n][n+1];
//         for(int i = 0; i < n; i++) {
//             for(int j = 0; j < n+1; j++) {
//                 dp[i][j] = -1;
//             }
//         }
//         return util(0, -1, n, nums, dp);
//     }

//     public int util(int curr, int prev, int n, int[] nums, int[][] dp) {
//         if(curr == n) return 0;
//         if(dp[curr][prev+1] != -1) return dp[curr][prev+1];
//         int length = util(curr+1, prev, n, nums, dp);
//         if(prev == -1 || nums[curr] > nums[prev]) {
//             length = Math.max(length, 1 + util(curr+1, curr, n, nums, dp));
//         }
//         dp[curr][prev+1] = length;
//         return length;
//     }
// }

// Time Complexity: O(n^2)
// Space Complexity: O(n^2) + O(n) due to spack space --> O(n^2)



// Tabulation
// Convert Memoization to Tabulation
// Code:
// class Solution {
//     public int lengthOfLIS(int[] nums) {
//         // Time Complexity: O(n^2)
//         // Space Complexity: O(n^2)
//         int n = nums.length;
//         int[][] dp = new int[n+1][n+1];
//         for(int curr = n-1; curr >= 0; curr--) {
//             for(int prev = curr-1; prev > -2; prev--) {
//                 int length = dp[curr+1][prev+1];
//                 if(prev == -1 || nums[curr] > nums[prev]) {
//                     length = Math.max(length, 1 + dp[curr+1][curr+1]);
//                 }
//                 dp[curr][prev+1] = length;                
//             }
//         }
//         return dp[0][0];
//     }
// }

// Time Complexity: O(n^2)
// Space Complexity: O(n^2)



// Space Optimization
// nums = [10,9,2,5,3,7,101,18]
// dp = [_, _, _, _, _, _, _, _]
// for last element value in dp = 1
// dp = [_, _, _, _, _, _, _, 1]
// Next for 101 --> go back to all numbers greater than 101 --> as no element is greater than 101, value in dp = 1
// dp = [_, _, _, _, _, _, 1, 1]
// Next for 7 --> go back to all numbers greater than 7 --> as 101 and 18 both are greater, value in dp = max(val in 101, val in 18) + 1 = 2
// dp = [_, _, _, _, _, 2, 1, 1]
// Next for 3 --> go back to all numbers greater than 3 --> as 7, 101, and 18 all are greater, value in dp = max(val in 7, val in 101, val in 18) + 1 = 3
// dp = [_, _, _, _, 3, 2, 1, 1]
// Next for 5 --> go back to all numbers greater than 5 --> as 7, 101, and 18 are greater, value in dp = max(val in 7, val in 101, val in 18) + 1 = 3
// dp = [_, _, _, 3, 3, 2, 1, 1]
// Next for 2 --> go back to all numbers greater than 2 --> as 5, 3, 7, 101, and 18 all are greater, value in dp = max(val in 5, val in 3, val in 7, val in 101, val in 18) + 1 = 4
// dp = [_, _, 4, 3, 3, 2, 1, 1]
// Next for 9 --> go back to all numbers greater than 9 --> as 101 and 18 are greater, value in dp = max(val in 101, val in 18) + 1 = 2
// dp = [_, 2, 4, 3, 3, 2, 1, 1]
// Next for 10 --> go back to all numbers greater than 10 --> as 101 and 18 are greater, value in dp = max(val in 101, val in 18) + 1 = 2
// dp = [2, 2, 4, 3, 3, 2, 1, 1]

// length of the longest strictly increasing subsequence is the max number in dp --> 4

// Code:
// class Solution {
//     public int lengthOfLIS(int[] nums) {
//         // Time Complexity: O(n^2)
//         // Space Complexity: O(n)
//         int n = nums.length;
//         if(n == 0) return 0;
//         int[] dp = new int[n];
//         dp[n-1] = 1;
//         int length = 1;
//         for(int i = n-2; i >= 0; i--) {
//             int maxnext = 0;
//             for(int j = i+1; j < n; j++) {
//                 if(nums[i] < nums[j]) {
//                     maxnext = Math.max(maxnext, dp[j]);
//                 }
//             }
//             dp[i] = 1 + maxnext;
//             length = Math.max(length, dp[i]);
//         }
//         return length;
//     }
// }

// Time Complexity: O(n^2)
// Space Complexity: O(n)



// Binary Search
// For each value we will find out if it can be added to an already existing increasing subsequence or we need to create a new increasing subsquence for it
// Example:
// nums = [10,9,2,5,3,7,101,18]
// for 10: create an increasing subsequence [10]
// for 9: create another increasing subsequence [10] [9]
// for 2: create another increasing subsequence [10] [9] [2]
// for 5: add it after 2, [10] [9] [2, 5]
// for 3: add it after 2, [10] [9] [2, 5] [2, 3]
// for 7: add it after 5 and 3, [10] [9] [2, 5, 7] [2, 3, 7]
// for 101: add it after all subsequences, [10, 101] [9, 101] [2, 5, 7, 101] [2, 3, 7, 101]
// for 18: add it after [10] [9] [2, 5, 7] [2, 3, 7], as [10, 101] [9, 101] [2, 5, 7, 101] [2, 3, 7, 101] [10, 18] [9, 18] [2, 5, 7, 18] [2, 3, 7, 18]
// so the length of longest increasing subsequence is 4.

// Instead of storing all the subsequences, we'll store then in a single array. If a value is larger than the last element of the array, we can simply append it at the end. Else, we'll look for the next greater element using binary search and replace it with the current element.

// Example:
// nums = [10,9,2,5,3,7,101,18]
// for 10: result = [10]
// for 9: result = [9]
// for 2: result = [2]
// for 5: result = [2, 5]
// for 3: result = [2, 3]
// for 7: result = [2, 3, 7]
// for 101: result = [2, 3, 7, 101]
// for 18: result = [2, 3, 7, 18]

// Note: The result may not always store the Longest Increasing Subsequence but its length is always equal to the length of longest increasing subsequence.

// Code:
// class Solution {
//     public int lengthOfLIS(int[] nums) {
//         // Time Complexity: O(nlogn)
//         // Space Complexity: O(n)
//         int n = nums.length;
//         if(n == 0) return 0;
//         int[] result = new int[n];
//         result[0] = nums[0];
//         int length = 1;
//         for(int i = 1; i < n; i++) {
//             if(result[length-1] < nums[i]) {
//                 result[length] = nums[i];
//                 length++;
//             }
//             else {
//                 int left = 0;
//                 int right = length-1;
//                 while(left < right) {
//                     int mid = (left+right)/2;
//                     if(result[mid] >= nums[i]) {
//                         right = mid;
//                     } else {
//                         left = mid+1;
//                     }
//                 }
//                 result[right] = nums[i];
//             }
//         }
//         return length;
//     }
// }

// Time Complexity: O(nlogn)
// Space Complexity: O(n)
