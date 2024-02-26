# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(h)
        if (not p and not q): return True
        if (not p or not q): return False
        if p.val != q.val: return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Approach:
# Base Cases:
    # If both p and q are None, return True, indicating that the subtrees rooted at p and q are identical.
    # If either p or q is None while the other is not, return False, indicating that the trees are not identical.
# If the values of the current nodes p and q are not equal, return False, indicating that the trees are not identical.
# If the values of the current nodes p and q are equal, recursively call the isSameTree function for the left subtrees (p.left and q.left) and the right subtrees (p.right and q.right).
# If all recursive calls return True, indicating that all corresponding subtrees are identical, return True.
# Otherwise, if any recursive call returns False, return False, indicating that the trees are not identical.
        
# Time Complexity: O(n)
# Space Complexity: O(h) where h is the height of the tree
