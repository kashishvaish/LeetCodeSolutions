# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        diameter = [0]
        self.height(root, diameter)
        return diameter[0]
        
    def height(self, node, diameter):
        if not node: return 0
        elif not node.left and not node.right: return 0
        l = 0
        r = 0
        if node.left:
            l = self.height(node.left, diameter) + 1
        if node.right: 
            r = self.height(node.right, diameter) + 1
        diameter[0] = max(diameter[0], l + r)
        return max(l, r)

# Approach:
# Initialize a variable diameter to store the diameter of the binary tree.
# Call the helper function height to calculate the height of the binary tree and update the diameter variable.
    # The height function calculates the height of the binary tree rooted at the given node and updates the diameter variable with the maximum diameter found so far.
    # If the current node is None, return 0.
    # Otherwise, recursively calculate the height of the left subtree (l) and the right subtree (r) of the current node.
    # Update the diameter variable with the maximum diameter found so far, which is the maximum of the sum of heights of the left and right subtrees plus 1 (representing the current node) and the current diameter value.
    # Return the maximum height of the left and right subtrees plus 1, representing the height of the subtree rooted at the current node.
# Return the diameter value as the result.

# Time Complexity: O(n)
# Space Complexity: O(n) due to the recursive calls on the call stack.
