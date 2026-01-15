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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        queue<TreeNode*> q1;
        queue<TreeNode*> q2;

        q1.push(p);
        q2.push(q);

        while(!q1.empty() && !q2.empty()){
            if(q1.size() != q2.size()){
                return false;
            }
            int size = q1.size();
            for(int i = 0; i<size; i++){
                TreeNode* p1 = q1.front();
                q1.pop();
                TreeNode* p2 = q2.front();
                q2.pop();

                if(p1==NULL && p2 == NULL){//both are NULL
                    continue;
                }
                if(p1==NULL || p2 == NULL){//One of the nodes are NULL
                    return false;
                }
                if(p1->val != p2->val){//values don't match
                    return false;
                }

                //push the next level
                q1.push(p1->left);
                q1.push(p1->right);
                q2.push(p2->left);
                q2.push(p2->right);
                
            }
        }
        return (q1.empty() && q2.empty());
    }
};