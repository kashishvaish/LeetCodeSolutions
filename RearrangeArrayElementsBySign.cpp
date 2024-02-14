class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        // Time Complexity: O(n)
        // Space Complexity: O(n)
        int n = nums.size();
        vector<int> ans(n, 0);
        int pos = 0;
        int neg = 1;
        for(int num: nums) {
            if(num > 0) {
                ans[pos] = num;
                pos += 2;
            } else {
                ans[neg] = num;
                neg += 2;
            }
        }
        return ans;
    }
};

// Naive Approach:
// Store positive and negative elements in separate arrays. Then modify the array nums using them.

// Example:
// nums = [3,1,-2,-5,2,-4]
// positive = [3, 1, 2]
// negatives = [-2, -5, -4]
// result nums = [3, -2, 1, -5, 2, -4]

// Time Complexity: O(n)
// Space Complexity: O(n)


// Two Pointer Approach:
// Initialize n to the size of nums.
// Initialze ans array of size n.
// Initialize two integers pos and neg with values 0 and 1 respectively.
// Traverse nums from the start.
// If the current integer is positive, set ans[pos] equal to it --> Increment pos by 2.
// If the current integer is negative, set ans[neg] equal to it --> Increment neg by 2.
// return ans array

// Time Complexity: O(n)
// Space Complexity: O(n)
