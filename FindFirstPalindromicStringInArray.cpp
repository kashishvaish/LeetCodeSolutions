class Solution {
public:
    string firstPalindrome(vector<string>& words) {
        // Time Complexity: O(n x m)
        // Space Complexity: O(1)
        for(string word: words) {
            int start = 0;
            int end = word.size() - 1;
            bool ispal = true;
            while(start < end) {
                if(word[start] != word[end]) {
                    ispal = false;
                    break;
                }
                start++;
                end--;
            }
            if(ispal) return word;
        }
        return "";
    }
};

// Approach:
// For each string check if it is palindrome or not using two pointers approach.
// Return the first palindromic string.
    
// Time Complexity: O(n x m)
// Space Complexity: O(1)
