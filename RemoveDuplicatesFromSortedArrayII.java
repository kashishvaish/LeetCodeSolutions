class Solution {
    public int removeDuplicates(int[] nums) {
        // Time Complexity: O(n)
        // Space Complexity: O(1)
        int n = nums.length;
        if(n <= 2) return n;
        int k = 2;
        int secondlast = nums[0];
        int last = nums[1];
        for(int i = 0; i < n; i++) {
            if(nums[i] != secondlast) {
                nums[k] = nums[i];
                k++;
            }
            secondlast = last;
            last = nums[i];
        }
        return k;
    }
}

// Approach:
// The idea is to iterate through the array and maintain a pointer k that keeps track of the position where the next valid element should be placed.
// Two variables secondlast and last are used to keep track of the last two elements encountered, ensuring that the current element is not a duplicate of the previous two.

// Time Complexity: O(n)
// Space Complexity: O(1)
