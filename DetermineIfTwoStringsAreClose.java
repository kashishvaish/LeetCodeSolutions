class Solution {
    public boolean closeStrings(String word1, String word2) {
        // Time Complexity: O(n)
        // Space Complexity: O(1)
        int m = word1.length();
        int n = word2.length();
        if(m != n) return false;
        int[] freq1 = new int[26];
        int[] freq2 = new int[26];
        for(int i = 0; i < n; i++) {
            freq1[(int)word1.charAt(i)-97]++;
            freq2[(int)word2.charAt(i)-97]++;
        }
        for(int i = 0; i < 26; i++) {
            if((freq1[i] == 0) != (freq2[i] == 0)) return false;
        }
        Arrays.sort(freq1);
        Arrays.sort(freq2);
        return Arrays.equals(freq1, freq2);
    }
}

// Approach
// If lengths are different, return False.
// Store the frequency of each letter in both strings.
// If a character is present in one word and not in another, return False.
// Two strings can be made close, if the values of frequencies are same, irrespective of the order.
// Sort the frequencies and compare them, if the sorted frequencies are equal --> return True, else --> return False.

// Time Complexity: O(n)
// Space Complexity: O(1)
