class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // Time Complexity: O(n x klogk)
        // Space Complexity: O(n x k)
        // Where k is the length of longest string
        HashMap<String, Integer> map = new HashMap<>();
        List<List<String>> result = new ArrayList<>(); 
        for(String s: strs) {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);
            if(map.containsKey(key)) {
                result.get(map.get(key)).add(s);
            } else {
                map.put(key, result.size());
                result.add(new ArrayList<>(Arrays.asList(s)));
            }
        }
        return result;
    }
}

// Approach:
// Iterate through each string in the input list.
// For each string, sort its characters to create a sorted string, which serves as a key for anagrams.
// This key is used to group anagrams together.
// Check if it exists in the hash table.
// If yes, the current word is appended to the corresponding list of anagrams.
// Else, a new key is created, and the current word is added to a new list associated with that key.
// Finally, the anagram groups are returned.

// Time Complexity: O(n x klogk) where k is the length of longest string
// Space Complexity: O(n x k) where k is the length of longest string
