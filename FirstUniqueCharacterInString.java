class Solution {
    public int firstUniqChar(String s) {
        // Time Complexity: O(n)
        // Space Complexity: O(1)
        int[] freq = new int[26];
        int n = s.length();
        for(int i = 0; i < n; i++) freq[(int)s.charAt(i) - 97]++;
        for(int i = 0; i < n; i++) {
            if(freq[(int)s.charAt(i)-97] == 1) return i; 
        }
        return -1;
    }
}

// Approach:
// Since string s only contains lowercase english alphabets,
// We can use an array of size 26 to store the frequency of each alphabet.
// Traverse over the characters of the string once to track the frequencies.
// Again, traverse the characters, if frequency of a character is 1, return its index.
// If no such element is found, return -1. 

// Time Complexity: O(n)
// Space Complexity: O(1)
