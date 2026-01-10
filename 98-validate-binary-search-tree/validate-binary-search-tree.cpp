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
    //Recursive DFS
    bool isValidBST(TreeNode* root) {
        return valid(root, LONG_MIN, LONG_MAX);
    }

    bool valid(TreeNode* node, long min, long max){
        if(node==NULL){
            return true;
        }
        if(!(min<node->val && max>node->val)){
            return false;
        }
        return (valid(node->left, min, node->val) && valid(node->right, node->val, max));
    }
};