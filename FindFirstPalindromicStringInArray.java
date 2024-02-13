class Solution {
    public String firstPalindrome(String[] words) {
        // Time Complexity: O(n x m)
        // Space Complexity: O(1)
        for(String word: words) {
            int start = 0;
            int end = word.length() - 1;
            boolean ispal = true;
            while(start <= end) {
                if(word.charAt(start) != word.charAt(end)) {
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
}

// Approach:
// For each string check if it is palindrome or not using two pointers approach.
// Return the first palindromic string.
    
// Time Complexity: O(n x m)
// Space Complexity: O(1)
