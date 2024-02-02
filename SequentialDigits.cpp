class Solution {
public:
    vector<int> sequentialDigits(int low, int high) {
        // Time Complexity: O(1)
        // Space Complexity: O(1)
        vector<int> res;
        for(int i = 1; i < 10; i++) {
            int n = i;
            while(n <= high) {
                if(low <= n && n <= high) {
                    res.push_back(n);
                }
                int d = n % 10;
                if(d == 9) break;
                n = n*10 + d + 1; 
            }
        }
        sort(res.begin(), res.end());
        return res;
    }
};

// Approach:
// Generate sequential digits within the given range by starting with each digit from 1 to 9.
// Iteratively construct sequential numbers from that starting digit.
// Each number is checked if it falls within the given range [low, high].
// If it does, the number is appended to the result list.
// Finally, the resulting list of sequential digits is sorted before being returned.
// The time complexity is considered O(1) because the loops' size is constant, being bounded by the fixed range of sequential digits [1, 9].

// Time Complexity: O(1)
// Space Complexity: O(1)
