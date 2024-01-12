class Solution {
public:
    bool halvesAreAlike(string s) {
        // Time Complexity: O(n)
        // Space Complexity: O(1)
        int n = s.size();
        int c1 = 0;
        int c2 = 0;
        unordered_set<char> vowels{'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        for(int i = 0; i < n/2; i++) {
            if(vowels.find(s[i]) != vowels.end()) c1++;
        }
        for(int i = n/2; i < n; i++) {
            if(vowels.find(s[i]) != vowels.end()) c2++;
        }
        return c1 == c2;
    }
};

// Approach:
// Count the number of vowels in each half. --> If equal, return True. Else, return False.

// Time Complexity: O(n)
// Space Complexity: O(1)
