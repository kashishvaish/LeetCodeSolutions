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
    int rangeSumBST(TreeNode* root, int low, int high) {
        // Time Complexity: O(n)
        // Space Complexity: O(n)
        int result = 0;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()) {
            TreeNode* node = q.front();
            q.pop();
            if(node == NULL) {
                continue;
            }
            if(low <= node->val && node->val <= high) {
                result += node->val;
            }
            q.push(node->left);
            q.push(node->right);
        }
        return result;
    }
};


// Breadth First Search
// Traverse all nodes --> Check for condition and add the values that fall within the range --> Return the sum

// Time Complexity: O(n)
// Space Complexity: O(n)
