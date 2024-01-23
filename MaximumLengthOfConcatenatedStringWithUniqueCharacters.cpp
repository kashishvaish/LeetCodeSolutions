class Solution {
public:
    int maxLength(vector<string>& arr) {
        // Time Complexity: O(2^n)
        // Space Complexity: O(n)
        int freq[26];
        memset(freq, 0, sizeof(freq));
        return util(arr, 0, arr.size(), freq);
    }

    int util(vector<string>& arr, int i, int n, int freq[]) {
        if(i == n) {
            int result = 0;
            for(int x = 0; x < 26; x++) result += freq[x];
            return result;
        }
        int result = util(arr, i+1, n, freq);
        int newfreq[26];
        for(int x = 0; x < 26; x++) newfreq[x] = freq[x];
        bool valid = true;
        for(char ch: arr[i]) {
            if(newfreq[int(ch)-97] > 0) {
                valid = false;
                break;
            }
            newfreq[int(ch)-97]++;
        }
        if(valid) {
            result = max(result, util(arr, i+1, n, newfreq));
        }
        return result;
    }
};

// Approach:
// Check for all sebsequences with unique characters, return the length of longest such subsequence.

// Time Complexity: O(2^n)
// Space Complexity: O(n)
