class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // Time Complexity: O(n x klogk)
        // Space Complexity: O(n x k)
        // Where k is the length of longest string
        unordered_map<string, int> map;
        vector<vector<string>> result;
        for(string s: strs) {
            string key = s;
            sort(key.begin(), key.end());
            if(map.find(key) != map.end()) {
                result[map[key]].push_back(s);
            } else {
                map[key] = result.size();
                result.push_back({s});
            }
        }
        return result;
    }
};

// Approach:
// Iterate through each string in the input list.
// For each string, sort its characters to create a sorted string, which serves as a key for anagrams.
// This key is used to group anagrams together.
// Check if it exists in the hash table.
// If yes, the current word is appended to the corresponding list of anagrams.
// Else, a new key is created, and the current word is added to a new list associated with that key.
// Finally, the anagram groups are returned.

// Time Complexity: O(n x klogk) where k is the length of longest string
// Space Complexity: O(n x k) where k is the length of longest string
