class Solution {
    public int reverse(int x) {
        // Time: O(log(n))
        // Space: O(1)
        int sign = (x < 0) ? -1 : 1;
        int num = Math.abs(x);
        int rev = 0;
        while(num > 0) {
            int d = num % 10;
            // d > 7 as Integer.MAX_VALUE = 2147483647
            if(rev > Integer.MAX_VALUE/10 || rev == Integer.MAX_VALUE/10 && d > 7) {
                return 0;
            }
            rev = rev * 10 + d;
            num /= 10;
        }
        return rev*sign;
    }
}

// Approach:

// Reverse the number one digit at a time --> check overflow on adding each digit --> return reverse if no overflow --> else return 0

// Time: O(log(n))
// Space: O(1)
