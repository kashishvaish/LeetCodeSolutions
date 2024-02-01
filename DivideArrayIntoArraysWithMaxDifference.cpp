class Solution {
public:
    vector<vector<int>> divideArray(vector<int>& nums, int k) {
        // Time Complexity: O(nlogn)
        // Space Complexity: O(logn)
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        for(int i = 0; i < nums.size(); i+=3) {
            if(nums[i+2] - nums[i] <= k) {
                result.push_back({nums[i], nums[i+1], nums[i+2]});
            } else return {};
        }
        return result;
    }
};

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
