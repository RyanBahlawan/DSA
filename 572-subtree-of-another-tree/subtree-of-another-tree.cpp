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
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if(!subRoot){//NULL subroot
            return true;
        }
        if(!root){//NULL root
            return false;
        }

        if(isSameTree(root, subRoot)){//subtrees are the same
            return true;
        } else{//check left and right subtree
            return(isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot));
        }
    }

    bool isSameTree(TreeNode* r, TreeNode* s){
        if(!r && !s){ //both nodes are NULL
            return true;
        }
        if((!r && s) || (r && !s)){ //one of the nodes is NULL
            return false;
        }

        if(r->val == s->val){ //same value
            return(isSameTree(r->left, s->left) && isSameTree(r->right, s->right));
        } else{ //not the same value
            return false;
        }
    }
};