# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        last = {}
        return self.util(root, 0, last)
        
    def util(self, root, level, last):
        if not root: return True
        if level % 2 == 0:
            if root.val % 2 == 0: return False
        else:
            if root.val % 2 != 0: return False
        if level not in last:
            last[level] = root.val
        else:
            if level % 2 == 0 and last[level] >= root.val: return False
            if level % 2 == 1 and last[level] <= root.val: return False
        last[level] = root.val
        return self.util(root.left, level+1, last) and self.util(root.right, level+1, last)

# Appraoch:
# The isEvenOddTree function initiates the DFS traversal and returns the result obtained from the helper function util.
# The util function performs the actual traversal and checks whether the tree satisfies the even-odd properties at each level.
# The dictionary last is used to store the last occured value at each level of the tree.
# In each recursive call, the function checks if the current node exists. If not, it returns True, indicating that the subtree rooted at this node satisfies the even-odd properties.
# At each level of the tree, the function checks whether the values of nodes adhere to the even-odd pattern based on the level:
# For even levels, it ensures that all node values are odd and in strictly increasing order from left to right.
# For odd levels, it ensures that all node values are even and in strictly decreasing order from left to right.
# If any node violates this pattern or if the current node's value is not greater (for even levels) or not smaller (for odd levels) than the last value encountered at its level, the function returns False, indicating that the tree is not an even-odd tree.
# If the traversal completes without encountering any violations, the function returns True, indicating that the tree satisfies the even-odd properties.

# Time Complexity: O(n)
# Space Complexity: O(n)
