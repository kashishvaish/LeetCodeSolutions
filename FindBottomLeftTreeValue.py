# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        res = [-1, -1, -1]
        res = self.util(root, 0, 0, res)
        return res[0]
    
    def util(self, root, depth, left, res):
        if not root: return res
        if depth > res[1]:
            res = [root.val, depth, left]           
        res = self.util(root.left, depth+1, left+1, res)
        res = self.util(root.right, depth+1, left-1, res)
        return res

# Approach:
# Maintain a result array res to store the leftmost value found so far along with its depth and leftmost position.
# At each node, compare the current depth with the maximum depth found so far (res[1]).
# If the current depth is greater, update res with the current node's value, depth, and leftmost position.
# The traversal continues recursively to the left and right subtrees, updating res accordingly.
# Finally, when the traversal completes, the leftmost value found at the maximum depth (res[0]) is returned as the bottom-left value of the binary tree.
    
# Time Complexity: O(n)
# Space Complexity: O(n)
