# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        result = 0
        queue = [root]
        while queue:
            node = queue.pop(0)
            if not node:
                continue
            if low <= node.val <= high:
                result += node.val
            queue.append(node.left)
            queue.append(node.right)
        return result

# Breadth First Search
# Traverse all nodes --> Check for condition and add the values that fall within the range --> Return the sum

# Time Complexity: O(n)
# Space Complexity: O(n)
