/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        // Time Complexity: O(m + n)
        // Space Complexity: O(m + n)
        if(leafNodes(root1).equals(leafNodes(root2))) {
            return true;
        }
        return false;
    }

    public List<Integer> leafNodes(TreeNode root) {
        List<Integer> nodes = new ArrayList();
        Stack<TreeNode> stack = new Stack<TreeNode>();
        stack.push(root);
        while(stack.size() != 0) {
            TreeNode node = stack.pop();
            if(node != null) {
                if(node.left == null && node.right == null) {
                    nodes.add(node.val);
                } else {
                    stack.push(node.left);
                    stack.push(node.right);
                }
            }
        }
        return nodes;
    }
}

// Depth First Search
// 1. Find the leaf value sequence of each tree using Depth First Search.
// 2. Compare them, if equal --> return True, else --> return False.

// Time Complexity: O(m + n)
// Space Complexity: O(m + n)
// Here, m and n are the lengths of the two trees.
