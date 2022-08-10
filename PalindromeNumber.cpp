class Solution {
public:
    bool isPalindrome(int x) {
        // Time: O(log(n))
        // Space: O(1)
        int copy = x;
        long rev = 0;
        while(copy > 0) {
            rev = rev*10 + copy%10;
            copy /= 10;
        }
        return x == rev;
    }
};

// Approach:

// Reverse the number --> compare
// Time: O(log(n))
// Space: O(1)
