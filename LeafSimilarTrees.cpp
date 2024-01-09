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
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        // Time Complexity: O(m + n)
        // Space Complexity: O(m + n)
        if (leafNodes(root1) == leafNodes(root2)) {
            return true;
        }
        return false;
    }

    vector<int> leafNodes(TreeNode* root) {
        vector<int> result;
        stack<TreeNode*> stack;
        stack.push(root);
        if(root == NULL) return result;
        while(!stack.empty()) {
            TreeNode* node = stack.top();
            stack.pop();
            if(node->left == NULL && node->right == NULL) {
                result.push_back(node->val);
            } else {
                if(node->left != NULL) stack.push(node->left);
                if(node->right != NULL) stack.push(node->right);
            }
        }
        return result;
    }
};

// Depth First Search
// 1. Find the leaf value sequence of each tree using Depth First Search.
// 2. Compare them, if equal --> return True, else --> return False.

// Time Complexity: O(m + n)
// Space Complexity: O(m + n)
// Here, m and n are the lengths of the two trees.
