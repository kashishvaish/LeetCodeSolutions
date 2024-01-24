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
    int pseudoPalindromicPaths (TreeNode* root) {
        // Time Complexity: O(n)
        // Space Complexity: O(n)
        int result = 0;
        stack<pair<TreeNode*, int>> stk;
        stk.push({root, 0});
        while(!stk.empty()) {
            auto [node, freq] = stk.top();
            stk.pop();
            freq ^= 1 << node->val;
            if(node->left == NULL && node->right == NULL) {
                if((freq & (freq-1)) == 0) result++;
            }
            if(node->left != NULL) stk.push({node->left, freq});
            if(node->right != NULL) stk.push({node->right, freq});
        }
        return result;
    }
};

// DFS
// Track frequency of elements in all paths from root node to leaf nodes.
// If atmost 1 value comes odd number of times in a path, the path can be considered as pseudo-palindromic.
// Return the total count of pseudo-palindromic paths found.

// Time Complexity: O(n)
// Space Complexity: O(n)


// Bit Manipulation
// Saving frequencies in a list is space consuming for large trees. To save space, we can compute parity using bitwise operators.
// We can keep the frequency of digit 1 in the first bit, 2 in the second bit, etc.
// Hence, the number of elements with odd frequencies can be tracked using, freq ^= (1 << node.val). Here, Left shift operator is used to define the bit, and XOR operator is used to compute the digit frequency. In a path only those bits are visible that appear an odd number of times.
// Now, to ensure that at most one digit has an odd frequency, check that path is a power of two, i.e., at most one bit is set to one. That could be done by turning off (= setting to 0) the rightmost 1-bit: freq & (freq - 1) == 0. To subtract 1 means to change the rightmost 1-bit to 0 and to set all the lower bits to 1.

// Time Complexity: O(n)
// Space Complexity: O(n)
