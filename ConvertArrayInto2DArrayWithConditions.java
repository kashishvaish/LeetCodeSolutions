class Solution {
    public List<List<Integer>> findMatrix(int[] nums) {
        // Time Complexity: O(n)
        // Space Complexity: O(n)
        int counts[] = new int[nums.length + 1];
        ArrayList<List<Integer>> res = new ArrayList<>();
        int maxfreq = 0;
        for (int i: nums) {
            if (maxfreq <= counts[i]) {
                res.add(new ArrayList<>());
            }
            res.get(counts[i]).add(i);
            counts[i]++;
            if (counts[i] > maxfreq) {
                maxfreq = counts[i];
            }
        }
        return res;
    }
}

// Intuition:
// Create an array of length n+1 to store the frequencies of elements in nums.
// Create an empty 2D array to store the result.
// For each integer i in nums -->
//   If the current max freq, is less than equal to the current frequency of i, add a row to the result array.
//   Append the integer i at the row with the index equal to current frequency of i.
//   Increase the frequency of i.
//   Track the maximum frequency.
// Return the result array.

// Time Complexity: O(n)
// Space Complexity: O(n)
