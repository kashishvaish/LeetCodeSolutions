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
    public int rangeSumBST(TreeNode root, int low, int high) {
        // Time Complexity: O(n)
        // Space Complexity: O(n)
        int result = 0;
        LinkedList<TreeNode> queue = new LinkedList<TreeNode>();
        queue.add(root);
        while(queue.size() != 0) {
            TreeNode node = queue.remove();
            if(node == null) {
                continue;
            }
            if(low <= node.val && node.val <= high){
                result += node.val;
            }
            queue.add(node.left);
            queue.add(node.right);
        }
        return result;
    }
}

// Breadth First Search
// Traverse all nodes --> Check for condition and add the values that fall within the range --> Return the sum

// Time Complexity: O(n)
// Space Complexity: O(n)
