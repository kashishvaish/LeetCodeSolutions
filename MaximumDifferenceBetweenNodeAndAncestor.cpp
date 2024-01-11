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
    int maxAncestorDiff(TreeNode* root) {
        // Time Complexity: O(n)
        // Space Complexity: O(n)
        return getmaxdiff(root, root->val, root->val);
    }

    int getmaxdiff(TreeNode* node, int maxval, int minval) {
        if(node == NULL) {
            return 0;
        }
        maxval = max(maxval, node->val);
        minval = min(minval, node->val);
        int maxdiff = max(getmaxdiff(node->left, maxval, minval), getmaxdiff(node->right, maxval, minval));
        maxdiff = max(maxdiff, maxval-minval);
        return maxdiff;
    }
};

// Approach:
// Recursively traverse the tree keeping track of the minimum and maximum value found in the path.
// Return the maximum difference between the maximum and minimum values.

// Time Complexity: O(n)
// Space Complexity: O(n)
