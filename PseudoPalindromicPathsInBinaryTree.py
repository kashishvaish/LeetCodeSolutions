# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        result = [0]
        self.util(root, 0, result)
        return result[0]

    def util(self, node, freq, result):
        freq ^= 1 << node.val 
        if(not node.left and not node.right):
            if freq & (freq-1) == 0:
                result[0] += 1
            return
        if(node.left): self.util(node.left, freq, result)
        if(node.right): self.util(node.right, freq, result)
        
# DFS
# Track frequency of elements in all paths from root node to leaf nodes.
# If atmost 1 value comes odd number of times in a path, the path can be considered as pseudo-palindromic.
# Return the total count of pseudo-palindromic paths found.

# Code:
# class Solution:
#     def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
#         # Time Complexity: O(n)
#         # Space Complexity: O(n)
#         result = [0]
#         self.util(root, [0]*10, result)
#         return result[0]

#     def util(self, node, freq, result):
#         freq[node.val] += 1
#         if(not node.left and not node.right):
#             odd = 0
#             for i in range(1, 10):
#                 if freq[i]%2 == 1: odd += 1
#                 if odd > 1:
#                     return
#             result[0] += 1
#             return
#         l = [x for x in freq]
#         r = [x for x in freq]
#         if(node.left): self.util(node.left, l, result)
#         if(node.right): self.util(node.right, r, result)

# Time Complexity: O(n)
# Space Complexity: O(n)


# Bit Manipulation
# Saving frequencies in a list is space consuming for large trees. To save space, we can compute parity using bitwise operators.
# We can keep the frequency of digit 1 in the first bit, 2 in the second bit, etc.
# Hence, the number of elements with odd frequencies can be tracked using, freq ^= (1 << node.val). Here, Left shift operator is used to define the bit, and XOR operator is used to compute the digit frequency. In a path only those bits are visible that appear an odd number of times.
# Now, to ensure that at most one digit has an odd frequency, check that path is a power of two, i.e., at most one bit is set to one. That could be done by turning off (= setting to 0) the rightmost 1-bit: freq & (freq - 1) == 0. To subtract 1 means to change the rightmost 1-bit to 0 and to set all the lower bits to 1.

# Code:
# class Solution:
#     def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
#         # Time Complexity: O(n)
#         # Space Complexity: O(n)
#         result = [0]
#         self.util(root, 0, result)
#         return result[0]

#     def util(self, node, freq, result):
#         freq ^= 1 << node.val 
#         if(not node.left and not node.right):
#             if freq & (freq-1) == 0:
#                 result[0] += 1
#             return
#         if(node.left): self.util(node.left, freq, result)
#         if(node.right): self.util(node.right, freq, result)

# Time Complexity: O(n)
# Space Complexity: O(n)
