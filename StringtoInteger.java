class Solution {
    public int myAtoi(String s) {
        // Time: O(n)
        // Space: O(1)
        s = s.trim();
        if(s.length() == 0) {
            return 0;
        }
        int i = 0;
        int sign = 1;
        if(s.charAt(0) == '-') {
            sign = -1;
            i += 1;
        } else if(s.charAt(0) == '+') {
            i += 1;
        }
        int res = 0;
        while(i < s.length() && Character.isDigit(s.charAt(i))) {
            int val = s.charAt(i) - '0';
            int temp = res*sign;
            if((temp < (Integer.MIN_VALUE/10)) || ((temp == (Integer.MIN_VALUE/10)) && val > 7)) {
                return Integer.MIN_VALUE;
            } else if(temp > Integer.MAX_VALUE/10 || (temp == Integer.MAX_VALUE/10 && val > 7)) {
                return Integer.MAX_VALUE;
            }
            res = res*10 + val;
            i += 1;
        }
        return res*sign;
    }
}

// Approach:

// 1. Remove leading whitespaces
// 2. if string is empty --> return 0
// 3. if first character is "-" --> set sign to -1 --> else, set sign to 1
// 4. for remaining characters till not digit is not found --> add digits to number
// 5. check for range
// 6. return number

// Time: O(n)
// Space: O(1)
