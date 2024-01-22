class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        // Time Complexity: O(n)
        // Space Complexity: O(1)
        int n = nums.size();
        int repeat;
        int miss;
        for(int i = 0; i < n; i++) {
            int ind = abs(nums[i])-1;
            if(nums[ind] < 0) repeat = abs(nums[i]);
            else nums[ind] *= -1; 
        }
        for(int i = 0; i < n; i++) {
            if(nums[i] > 0) {
                miss = i+1;
                break;
            }
        }
        return {repeat, miss};
    }
};

// Approach: 
// Store the frequencies of each element.
// Return the elements with 0 and 2 frequencies.

// Time Complexity: O(n)
// Space Complexity: O(n)



// Space Optimization:
// We will traverse through the numbers and since the numbers are in the range 1 to n, we will make the number with index equal to element - 1 negative. This will indicate the occurence of the element. If a number is already negative, it will indicate duplicacy. To identify the missing number, we'll iterate again to find the index with positive number.

// Code:
// class Solution {
// public:
//     vector<int> findErrorNums(vector<int>& nums) {
//         // Time Complexity: O(n)
//         // Space Complexity: O(1)
//         int n = nums.size();
//         int repeat;
//         int miss;
//         for(int i = 0; i < n; i++) {
//             int ind = abs(nums[i])-1;
//             if(nums[ind] < 0) repeat = abs(nums[i]);
//             else nums[ind] *= -1; 
//         }
//         for(int i = 0; i < n; i++) {
//             if(nums[i] > 0) {
//                 miss = i+1;
//                 break;
//             }
//         }
//         return {repeat, miss};
//     }
// };

// Time Complexity: O(n)
// Space Complexity: O(1)
