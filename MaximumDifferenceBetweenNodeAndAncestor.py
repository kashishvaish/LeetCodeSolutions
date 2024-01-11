# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n) 
        return self.getmaxdiff(root, root.val, root.val)

    def getmaxdiff(self, node, minval, maxval):
        if not node:
            return 0
        minval = min(minval, node.val)
        maxval = max(maxval, node.val)
        maxdiff = max(maxval-minval, self.getmaxdiff(node.left, minval, maxval), self.getmaxdiff(node.right, minval, maxval))
        return maxdiff

# Approach:
# Recursively traverse the tree keeping track of the minimum and maximum value found in the path.
# Return the maximum difference between the maximum and minimum values.

# Time Complexity: O(n)
# Space Complexity: O(n)
