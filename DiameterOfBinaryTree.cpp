/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        // Time Complexity: O(n)
        // Space Complexity: O(n)
        int diameter = 0;
        util(root, diameter);
        return diameter;
    }
    
    int util(TreeNode* node, int& diameter) {
        if(node == NULL || (node->left == NULL && node->right == NULL)) return 0;
        int l = 0;
        int r = 0;
        if(node->left != NULL) l = util(node->left, diameter) + 1;
        if(node->right != NULL) r = util(node->right, diameter) + 1;
        diameter = max(diameter, l+r);
        return max(l, r);
    }
    
};

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
