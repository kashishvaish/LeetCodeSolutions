class Solution {
    public int findContentChildren(int[] g, int[] s) {
        // Time Complexity: O(nlogn + mlogm)
        // Space Complexity: O(logn + logm)
        Arrays.sort(g);
        Arrays.sort(s);
        int c = 0;
        int j = s.length-1;
        for(int i = g.length-1; i >= 0; i--) {
            if (j < 0) {
                break;
            }
            if (g[i] > s[j]) {
                continue;
            }
            else {
                c += 1;
                j -= 1;
            }
        }
        return c;
    }
}

// Intuition - Greedy, Two-Pointer:
// Sort both greed and sizes arrays.
// Start allocating the largest available cookie to the children starting from the child with highest greed to lowest greed.
// Stop if no more cookies are left to assign.

// Time Complexity: O(nlogn + mlogm) due to sorting
// Space Complexity: O(logn + logm) due to sorting
