class Solution {
    public List<List<Integer>> findWinners(int[][] matches) {
        // Time Complexity: O(nlogn)
        // Space Complexity: O(n)        
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int[] i: matches) {
            if (!map.containsKey(i[0])) {
                map.put(i[0], 0);
            }
            if (!map.containsKey(i[1])) {
                map.put(i[1], 0);
            }
            map.put(i[1], map.get(i[1])+1);
        }
        List<Integer> zero = new ArrayList<>();
        List<Integer> one = new ArrayList<>();
        for(Map.Entry<Integer, Integer> set : map.entrySet()) {
            if(set.getValue() == 0) {
                zero.add(set.getKey());
            } else if(set.getValue() == 1) {
                one.add(set.getKey());
            }
        }
        Collections.sort(zero);
        Collections.sort(one);
        List<List<Integer>> result = new ArrayList<>();
        result.add(zero);
        result.add(one);
        return result;
    }
}

// Approach:
// Create a dictionary/hashmap to store the players and their number of losses.
// Store players with 0 and 1 losses in different lists.
// Sort them and return the answer.

// Time Complexity: O(nlogn)
// Space Complexity: O(n)
