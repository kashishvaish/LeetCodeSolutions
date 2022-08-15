class Solution {
    public int maxArea(int[] height) {
        // Time: O(n)
        // Space: O(1)
        int left = 0;
        int right = height.length-1;
        int maxCapacity = 0;
        while(left < right) {
            maxCapacity = Math.max(maxCapacity, Math.min(height[left], height[right])*(right-left));
            if(height[left] > height[right]) {
                right -= 1;
            } else if(height[left] < height[right]) {
                left += 1;
            } else {
                left += 1;
                right -= 1;
            }
        }
        return maxCapacity;
    }
}

// Approach

// Brute Force Approach:

// For every pair of lines calculate capacity of water that can be stored --> return maximum capacity
// Time: O(n^2)
// Space: O(1)

// Two Pointers:

// Take two pointers left and right initially at start and end of the array
// Intuition:
// if height at left index > height at right index --> move right pointer towards left
// else if height at left index < height at right index --> move left pointer towards right
// else move right pointer one step towards left and right pointer one step towards left
// keep track of maximum capacity found

// Time: O(n)
// Space: O(1)
