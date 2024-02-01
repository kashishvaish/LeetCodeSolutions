class Solution {
    public int[][] divideArray(int[] nums, int k) {
        // Time Complexity: O(nlogn)
        // Space Complexity: O(logn)
        int n = nums.length;
        Arrays.sort(nums);
        int[][] result = new int[n/3][3];
        for(int i = 0; i < n; i+=3) {
            if(nums[i+2] - nums[i] <= k) {
                result[i/3][0] = nums[i];
                result[i/3][1] = nums[i+1];
                result[i/3][2] = nums[i+2];
            } else return new int[0][0];
        }
        return result;
    }
}

// Approach:
// Sort the array in ascending order.
// Iterate through the sorted array in steps of 3.
// For each group of three consecutive elements,
//   Check if maximum - minimum <= k.
//   If yes, append the current group to the result list.
//   Else, immediately return an empty list, indicating that it's not possible to divide the array as required.
// Finally, return the resulting list of subarrays.

// Time Complexity: O(nlogn)
// Space Complexity: O(logn)
