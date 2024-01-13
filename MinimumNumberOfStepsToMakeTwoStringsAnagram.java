class Solution {
    public int minSteps(String s, String t) {
        // Time Complexity: O(n)
        // Space Complexity: O(1)
        int[] freq = new int[26];
        for(int i = 0; i < s.length(); i++) {
            freq[(int)s.charAt(i)-97]++;
            freq[(int)t.charAt(i)-97]--;
        }
        int result = 0;
        for(int i = 0; i < 26; i++) {
            if(freq[i] > 0) result += freq[i];
        }
        return result;
    }
}

// Approach:
// To make the strings anagrams, we do not need to consider thr instances if characters that are present in both the strings. Therefore, the problem comes down to counting the number of characters that are different in both strings.
// To do this, we can store the difference of frequencies of each character in an array. The result will be either of the sum of all positive differences or the sum of all negative differences.

// Time Complexity: O(n)
// Space Complexity: O(1)
