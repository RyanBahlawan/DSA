class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int prefix = 1;
        int postfix = 1;
        vector<int> res(nums.size(), 1);

        //for prefix
        for(int i = 0; i<nums.size(); i++){
            res[i] *= prefix;
            prefix *= nums[i];
        }

        //for postfix
        for(int j = (nums.size()-1); j>=0; j--){
            res[j] *= postfix;
            postfix *= nums[j];
        }

        return res;
    }
};