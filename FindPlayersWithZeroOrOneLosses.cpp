class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        // Time Complexity: O(n)
        // Space Complexity: O(n)
        map<int, int> losses;
        for(auto m: matches) {
            if(losses.find(m[0]) == losses.end()) {
                losses[m[0]] = 0;
            }
            losses[m[1]]++;
        }
        vector<int> zero, one;
        for(auto [p,l]: losses) {
            if(l == 0) zero.push_back(p);
            else if(l == 1) one.push_back(p);
        }
        return {zero, one};
    }
};

// Approach:
// Create an ordered map to store the players and their number of losses.
// Store players with 0 and 1 losses in different lists and return them.

// Time Complexity: O(n)
// Space Complexity: O(n)
