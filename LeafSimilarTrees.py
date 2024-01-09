# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Time Complexity: O(m + n)
        # Space Complexity: O(m + n)
        if self.leafvalue(root1) == self.leafvalue(root2):
            return True
        return False

    def leafvalue(self, root):
        leafnodes = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if node.left == None and node.right == None:
                    leafnodes.append(node.val)
                else:
                    stack.append(node.left)
                    stack.append(node.right)
        return leafnodes

# Depth First Search
# 1. Find the leaf value sequence of each tree using Depth First Search.
# 2. Compare them, if equal --> return True, else --> return False.

# Time Complexity: O(m + n)
# Space Complexity: O(m + n)
# Here, m and n are the lengths of the two trees.
