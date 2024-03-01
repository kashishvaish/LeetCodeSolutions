class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # Time complexity: O(n)
        # Space complexity: O(n)
        zero = s.count("0")
        one = s.count("1")
        return "1"*(one-1) + "0"*zero + "1"

# Approach:
# A binary string is odd if and only if the last bit (i.e. the one's place) equals 1.
# To rearrange bits in such a way as to maximize the value of the binary number, we should opt to swap as many 1 bits to the left as we can. This is because the more left a digit is, the more value it holds.
# For this, count the number of zeros and ones in the string.
# The desired binary number would be equal to "1"*(no_of_ones -1) + "0"*no_of_zeros + "1"

# Time complexity: O(n)
# Space complexity: O(n)
