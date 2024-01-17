class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        // Time Complexity: O(n)
        // Space Complexity: O(n)
        HashMap<Integer, Integer> freq = new HashMap<>();
        for(int i: arr) {
            freq.put(i, freq.getOrDefault(i, 0)+1);
        }
        Set<Integer> uniques = new HashSet<>();
        for(int i: freq.values()) {
            if(uniques.contains(i)) {
                return false;
            }
            uniques.add(i);
        }
        return true;
    }
}

// Approach:
// Store the elements and their corresponding frequencies in a hashmap.
// Iterate over the hashmap to check for repeating values.

// Time Complexity: O(n)
// Space Complexity: O(n)
