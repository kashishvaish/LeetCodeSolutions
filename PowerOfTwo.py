class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        return n > 0 and n & n-1 == 0 
        
# Approach 1:
# Check if n > 0 and number of 1's in binary representation of n is equal to 1.

# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         return n > 0 and bin(n).count("1") == 1


# Approach 2:
# Intuition - pow(2, n) & (pow(2, n) - 1) == 0
# for example,
# num = 4 = 0b100
# 4 - 1 = 3 = 0b11
# 4 & 3 = 0b100 & 0b11 = 0

# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         return n > 0 and n & n-1 == 0

# Time Complexity: O(1)
# Space Complexity: O(1)
