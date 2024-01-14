class Solution {
public:
    bool closeStrings(string word1, string word2) {
        // Time Complexity: O(n)
        // Space Complexity: O(1)
        int m = word1.size();
        int n = word2.size();
        if(m != n) return false;
        int freq1[26];
        int freq2[26];
        memset(freq1, 0, sizeof(freq1));
        memset(freq2, 0, sizeof(freq2));
        for(int i = 0; i < n; i++) {
            freq1[int(word1[i])-97]++;
            freq2[int(word2[i])-97]++;
        }
        for(int i = 0; i < 26; i++) {
            if((freq1[i]==0) != (freq2[i]==0)) {
                return false;
            }
        }
        sort(freq1, freq1+26);
        sort(freq2, freq2+26);
        for(int i = 0; i < 26; i++) {
            if(freq1[i] != freq2[i]) {
                return false;
            }
        }
        return true;
    }
};

// Approach
// If lengths are different, return False.
// Store the frequency of each letter in both strings.
// If a character is present in one word and not in another, return False.
// Two strings can be made close, if the values of frequencies are same, irrespective of the order.
// Sort the frequencies and compare them, if the sorted frequencies are equal --> return True, else --> return False.

// Time Complexity: O(n)
// Space Complexity: O(1)
