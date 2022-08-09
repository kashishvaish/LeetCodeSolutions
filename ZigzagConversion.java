class Solution {
    public String convert(String s, int numRows) {
        // Time: O(n)
        // Space: O(n)
        if(numRows == 1) return s;
        
        int curr = 0;
        boolean up = false;
        String[] pattern = new String[numRows];
        
        for(int i = 0; i < numRows; i++) {
            pattern[i] = "";
        }
        
        for(int i = 0; i < s.length(); i++) {
            pattern[curr] += s.charAt(i);
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
        
        String result = "";
        for(int i = 0; i < numRows; i++) {
            result += pattern[i];
        }
        return result;
    }
}

// Approach:

// Traverse through the string --> append each character to the row it belongs to using current row index and direction (up / down) --> merge rows.

// Time: O(n)
// Space: O(n)
