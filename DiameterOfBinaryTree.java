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
    int diameter;
    
    public int diameterOfBinaryTree(TreeNode root) {
        // Time Complexity: O(n)
        // Space Complexity: O(n)
        diameter = 0;
        util(root);
        return diameter;
    }
    
    public int util(TreeNode node) {
        if(node == null || (node.left == null && node.right == null)) return 0;
        int l = 0;
        int r = 0;
        if(node.left != null) l = util(node.left) + 1;
        if(node.right != null) r = util(node.right) + 1;
        diameter = Math.max(diameter, l+r);
        return Math.max(l, r);
    }
}

// Approach:
// Initialize a variable diameter to store the diameter of the binary tree.
// Call the helper function height to calculate the height of the binary tree and update the diameter variable.
//     The height function calculates the height of the binary tree rooted at the given node and updates the diameter variable with the maximum diameter found so far.
//     If the current node is None, return 0.
//     Otherwise, recursively calculate the height of the left subtree (l) and the right subtree (r) of the current node.
//     Update the diameter variable with the maximum diameter found so far, which is the maximum of the sum of heights of the left and right subtrees plus 1 (representing the current node) and the current diameter value.
//     Return the maximum height of the left and right subtrees plus 1, representing the height of the subtree rooted at the current node.
// Return the diameter value as the result.

// Time Complexity: O(n)
// Space Complexity: O(n) due to the recursive calls on the call stack.
