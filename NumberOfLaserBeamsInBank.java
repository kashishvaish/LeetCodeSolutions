class Solution {
    public int numberOfBeams(String[] bank) {
        // Time Complexity: O(mn)
        // Space Complexity: O(1)
        int total = 0;
        int current = 0;
        for(String s: bank) {
            int devices = 0;
            for(int i = 0; i < s.length(); i++) {
                if(s.charAt(i) == '1') {
                    devices++;
                }
            }
            if(devices != 0) {
                total += devices * current;
                current = devices;
            }
        }
        return total;
    }
}

// Intuition:
// We can count the number of laser beams by keeping track of the number of security devices in the previous row, ignoring the rows without safety devices.

// Time Complexity: O(mn)
// Space Complexity: O(1)
