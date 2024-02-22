class Solution {
    public int findJudge(int n, int[][] trust) {
        // Time Complexity: O(n + m)
        // Space Complexity: O(n)
        int[] in = new int[n+1];
        int[] out = new int[n+1];
        for(int[] t: trust) {
            out[t[0]]++;
            in[t[1]]++;
        }
        for(int i = 1; i <= n; i++) {
            if(in[i] == n-1 && out[i] == 0) return i;
        }
        return -1;
    }
}

// Approach:
// Create two arrays in and out, each of size n+1.
// The in array tracks the number of people who trust each person, while the out array tracks the number of people trusted by each person.
// Iterate through each trust relationship [u, v] in the trust array.
// For each trust relationship, increment the out count for the trusting person u and the in count for the trusted person v.
// Iterate through each person in the town from 1 to n.
// Check if the person is trusted by n-1 people (in[i] == n-1) and if the person trusts nobody (out[i] == 0).
// If both conditions are met for a person, return that person's label as the town judge.
// If no such person is found after iterating through all people, return -1 to indicate that there is no town judge.

// Time Complexity: O(n + m)
// Space Complexity: O(n)
