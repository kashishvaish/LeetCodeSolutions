class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Time: O(n)  Space: O(n)
        unordered_map<int, int> map;
        vector<int> result;
        for(int i=0; i < nums.size(); i++) {
            if(map.find(target - nums[i]) != map.end()) {
                result.push_back(map[target - nums[i]]);
                result.push_back(i);
                return result;
            }
            map[nums[i]] = i;
        }
        return result;
    }
};

// Approach

// 1. Brute Force Approach

// For all possible pairs, find their sum --> if sum == target for a pair: return indices of those elements.
// Time: O(n^2)
// Space: O(1)

// 2. Using HashMap

// Store elements and their indices as key and pairs in a HashMap, while traversing through the vector --> if target - element is present in the HashMap --> return index of target-element and element.
// Time: O(n)
// Space: O(n)
