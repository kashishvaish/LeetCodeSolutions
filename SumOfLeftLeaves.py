# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        result = [0]
        self.util(root, False, result)
        return result[0]
    
    def util(self, node, isLeft, result):
        if not node: return
        if not node.left and not node.right and isLeft: result[0] += node.val
        if node.left: self.util(node.left, True, result)
        if node.right: self.util(node.right, False, result)
            
# Approach:
# Initialize result as a list with one element initialized to 0. This list will store the sum of left leaves.

# Recursive Function:
# Define a helper function util that takes three parameters: node, isLeft, and result.
# If the current node is None, return.
# Check if the current node is a leaf node and is on the left side (determined by the isLeft parameter being True):
# If so, add the value of the leaf node to the first element of the result list.
# Recursively call the util function for the left and right child nodes, passing the appropriate isLeft value (True for the left child and False for the right child) and the result list.

# Main Function:
# Call the util function with the root node, setting isLeft to False initially, and passing the result list.
# Return the value stored in the first element of the result list, which now contains the sum of left leaves.

# Time Complexity: O(n)
# Space Complexity: O(n)
