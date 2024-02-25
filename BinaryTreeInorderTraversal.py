# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        res = []
        self.util(root, res)
        return res
    
    def util(self, node, res):
        if not node: return
        self.util(node.left, res)
        res.append(node.val)
        self.util(node.right, res)

# Approach:
# Perform an inorder traversal of a binary tree recursively.
# Start by checking if the current node exists.
# If it does, traverse the left subtree recursively, append the value of the current node to the result list, and then traverses the right subtree recursively.
# This process continues until all nodes in the tree have been visited.
# Finally, the list containing the inorder traversal result is returned.

# Time Complexity: O(n)
# Space Complexity: O(n)
