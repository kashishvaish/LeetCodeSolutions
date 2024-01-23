class Solution {
    public int maxLength(List<String> arr) {
        // Time Complexity: O(2^n)
        // Space Complexity: O(n)
        return util(arr, 0, arr.size(), new int[26]);
    }

    public int util(List<String> arr, int i, int n, int[] freq) {
        if(i == n) {
            int result = 0;
            for(int x: freq) result += x;
            return result;
        }
        int result = util(arr, i+1, n, freq);
        int[] newfreq = new int[26];
        for(int x = 0; x < 26; x++) {
            newfreq[x] = freq[x];
        }
        boolean valid = true;
        for(int x = 0; x < arr.get(i).length(); x++) {
            if(newfreq[(int)arr.get(i).charAt(x) - 97] > 0) {
                valid = false;
                break;
            }
            newfreq[(int)arr.get(i).charAt(x) - 97]++;
        }
        if(valid) {
            result = Math.max(result, util(arr, i+1, n, newfreq));
        }
        return result;
    }
}

// Approach:
// Check for all sebsequences with unique characters, return the length of longest such subsequence.

// Time Complexity: O(2^n)
// Space Complexity: O(n)
