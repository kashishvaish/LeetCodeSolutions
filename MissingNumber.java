class Solution {
    public int missingNumber(int[] nums) {
        // Time Complexity: O(n)
        // Space Complexity: O(1)
        int n = nums.length;
        int sum = 0;
        for(int num: nums) sum += num;
        return (n * (n+1) / 2) - sum;
    }
}

// Bitwise XOR
// XOR operation on a number with itself results in 0. 
// XOR all the numbers from 0 to n and all the numbers in the array, the result will be the missing number.

// Time Complexity: O(n)
// Space Complexity: O(1)



// Mathematical Formula
// Use the formula (n*(n+1)/2) to calculate the sum of the first n numbers.
// Subtract the sum of the array from it.
// The result is the missing number.

// Time Complexity: O(n)
// Space Complexity: O(1)
