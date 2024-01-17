class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        // Time Complexity: O(n)
        // Space Complexity: O(n)
        unordered_map<int, int> freq;
        for(int i: arr) {
            freq[i]++;
        }
        unordered_set<int> uniques;
        for(auto [v,f]: freq) {
            if(uniques.find(f) != uniques.end()) {
                return false;
            }
            uniques.insert(f);
        }
        return true;
    }
};

// Approach:
// Store the elements and their corresponding frequencies in a hashmap.
// Iterate over the hashmap to check for repeating values.

// Time Complexity: O(n)
// Space Complexity: O(n)
