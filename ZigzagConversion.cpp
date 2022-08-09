class Solution {
public:
    string convert(string s, int numRows) {
        // Time: O(n)
        // Space: O(n)
        if(numRows == 1) return s;
        
        string pattern[numRows];
        int curr = 0;
        bool up = false;
        for(char ch: s) {
            pattern[curr] += ch;
            if(!up && curr == numRows-1) {
                curr -= 1;
                up = true;
            } else if(!up) {
                curr += 1;
            } else if(up && curr == 0) {
                curr += 1;
                up = false;
            } else {
                curr -= 1;
            }
        }
        string result;
        for(string row: pattern) {
            result += row;
        }
        return result;
    }
};

// Approach:

// Traverse through the string --> append each character to the row it belongs to using current row index and direction (up / down) --> merge rows.

// Time: O(n)
// Space: O(n)
