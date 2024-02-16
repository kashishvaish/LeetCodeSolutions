class Solution {
    public int findLeastNumOfUniqueInts(int[] arr, int k) {
        // Time Complexity: O(nlogn)
        // Space Complexity: O(n)
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int num: arr) map.put(num, map.getOrDefault(num, 0) + 1);
        List<Integer> freqs = new ArrayList<>(map.values());
        Collections.sort(freqs);
        int total = freqs.size();
        for(int freq: freqs) {
            if(freq <= k) {
                total -= 1;
                k -= freq;
            } else break;
        }
        return total;
    }
}

// Approach:
// Use a hashmap to calculate the frequencies of elements in arr.
// Store the frequencies in an array and sort them in ascending order.
// Iterate over the sorted array to remove at most k elements, keeping track of the elements completely removed.
// Return the remaining number of unique elements.

// Time Complexity: O(nlogn)
// Space Complexity: O(n)
