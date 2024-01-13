class Solution {
public:
    int minSteps(string s, string t) {
        // Time Complexity: O(n)
        // Space Complexity: O(1)
        int freq[26];
        memset(freq, 0, sizeof(freq));
        for(int i = 0; i < s.size(); i++) {
            freq[int(s[i])-97]++;
            freq[int(t[i])-97]--;
        }
        int result = 0;
        for(int i = 0; i < 26; i++) {
            if(freq[i] > 0) result += freq[i];
        }
        return result;
    }
};

// Approach:
// To make the strings anagrams, we do not need to consider thr instances if characters that are present in both the strings. Therefore, the problem comes down to counting the number of characters that are different in both strings.
// To do this, we can store the difference of frequencies of each character in an array. The result will be either of the sum of all positive differences or the sum of all negative differences.

// Time Complexity: O(n)
// Space Complexity: O(1)
