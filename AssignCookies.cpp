class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        // Time Complexity: O(nlogn + mlogm)
        // Space Complexity: O(logn + logm)
        sort(g.begin(), g.end(), greater<int>());
        sort(s.begin(), s.end(), greater<int>());
        int c = 0;
        int j = 0;
        for(int i = 0; i < g.size(); i++) {
            if(j >= s.size()) {
                break;
            }
            else if(g[i] > s[j]) {
                continue;
            }
            else {
                c += 1;
                j += 1;
            }
        }
        return c;
    }
};

// Intuition - Greedy, Two-Pointer:
// Sort both greed and sizes arrays.
// Start allocating the largest available cookie to the children starting from the child with highest greed to lowest greed.
// Stop if no more cookies are left to assign.

// Time Complexity: O(nlogn + mlogm) due to sorting
// Space Complexity: O(logn + logm) due to sorting
