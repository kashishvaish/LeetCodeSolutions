class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Time: O(n)  Space: O(n)
        HashMap<Integer, Integer> map = new HashMap<>();
        int[] result = new int[2];
        for(int i = 0; i < nums.length; i++) {
            if(map.containsKey(target-nums[i])) {
                result[0] = map.get(target-nums[i]);
                result[1] = i;
                return result;
            }
            map.put(nums[i], i);
        }
        return result;
    }
}

// Approach

// 1. Brute Force Approach

// For all possible pairs, find their sum --> if sum == target for a pair: return indices of those elements.
// Time: O(n^2)
// Space: O(1)

// 2. Using HashMap

// Store elements and their indices as key and pairs in a HashMap, while traversing through the vector --> if target - element is present in the HashMap --> return index of target-element and element.
// Time: O(n)
// Space: O(n)
