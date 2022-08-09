class Solution {
public:
    int reverse(int x) {
        // Time: O(log(n))
        // Space: O(1)
        int sign = (x < 0) ? -1 : 1;
        long num = abs(x);
        long rev = 0;
        while(num) {
            int d = num % 10;
            rev = rev*10 + d;
            if(rev > pow(2, 31)) return 0;
            num = num / 10;
        }
        return rev*sign;
    }
};

// Approach:

// Reverse the number one digit at a time --> check overflow on adding each digit --> return reverse if no overflow --> else return 0

// Time: O(log(n))
// Space: O(1)
