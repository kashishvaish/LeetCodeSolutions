# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        result = [0]
        self.util(root, result, 0)
        return result[0]
    
    def util(self, node, result, val):
        if not node: return
        val = val*10 + node.val
        if not node.left and not node.right:
            result[0] += val
            return
        self.util(node.left, result, val)
        self.util(node.right, result, val)
        
# Approach:
# Initialize result as a list with one element initialized to 0. This list will store the sum of all root-to-leaf paths.
# Recursive Function:
# Define a helper function util that takes three parameters: node, result, and val.
# If the current node is None, return.
# Update the val by multiplying it by 10 and adding the value of the current node.
# If the current node is a leaf node (i.e., it has no left or right child), add the current val to the first element of the result list, representing the sum of the path.
# Recursively call the util function for the left and right child nodes, passing the updated val and the result list.
# Main Function:
# Call the util function with the root node, passing the result list initialized in step 1 and an initial val of 0.
# Return the value stored in the first element of the result list, which now contains the sum of all root-to-leaf paths.

# Time Complexity: O(n)
# Space Complexity: O(n)
