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
    public int maxAncestorDiff(TreeNode root) {
        // Time Complexity: O(n)
        // Space Complexity: O(n)
        return getmaxdiff(root, root.val, root.val);
    }

    public int getmaxdiff(TreeNode node, int maxval, int minval) {
        if(node == null) {
            return 0;
        }
        maxval = Math.max(maxval, node.val);
        minval = Math.min(minval, node.val);
        int maxdiff = Math.max(getmaxdiff(node.left, maxval, minval), getmaxdiff(node.right, maxval, minval));
        maxdiff = Math.max(maxdiff, maxval-minval);
        return maxdiff;
    }
}

// Approach:
// Recursively traverse the tree keeping track of the minimum and maximum value found in the path.
// Return the maximum difference between the maximum and minimum values.

// Time Complexity: O(n)
// Space Complexity: O(n)
