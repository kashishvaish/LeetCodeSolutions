class Solution {
public:
    int myAtoi(string s) {
        // Time: O(n)
        // Space: O(1)
        int i = 0;
        while(s[i] == ' ') {
            i += 1;
        }
        int sign = 1;
        if(s[i] == '-') {
            sign = -1;
            i += 1;
        } else if(s[i] == '+') {
            i += 1;
        }
        long num = 0;
        while(isdigit(s[i])) {
            num = num*10 + (int)(s[i])-(int)'0';
            if(num > pow(2, 31)) {
                if(sign == -1) {
                    return pow(-2, 31);
                }
                return pow(2, 31)-1;
            }
            i += 1;
        }
        num *= sign;
        if(num < pow(-2, 31)) {
            return pow(-2, 31);
        } else if(num > pow(2, 31)-1) {
            return pow(2, 31)-1;
        }
        return num;
    }
};

// Approach:

// 1. Remove leading whitespaces
// 2. if string is empty --> return 0
// 3. if first character is "-" --> set sign to -1 --> else, set sign to 1
// 4. for remaining characters till not digit is not found --> add digits to number
// 5. check for range
// 6. return number

// Time: O(n)
// Space: O(1)
