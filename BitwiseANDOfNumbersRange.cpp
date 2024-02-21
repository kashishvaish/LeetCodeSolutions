class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        // Time Complexity: O(1)
        // Space Complexity: O(1)
        int count = 0;
        while(left != right) {
            left >>= 1;
            right >>= 1;
            count++;
        }
        return left << count;
    }
};

// Approach:
// The bitwise AND operation between two numbers results in a number where each bit is 1 if and only if the corresponding bits of both numbers are 1.
// When considering a range [left, right], if the two numbers have different bits in any position, then the result of the AND operation will have a 0 in that position.
// So, we only need to find the common prefix of the binary representation of left and right.
// Any bits that differ between left and right will be set to 0 in the result.

// Time Complexity: O(1)
// Space Complexity: O(1)
