class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        if(nums.size()==0){
            return {};
        }
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        for(int i = 0; i<nums.size(); i++){
            if(nums[i]>0){
                break;
            }
            while(i>0 && i<nums.size() && nums[i]==nums[i-1]){
                i++;
            }
            int l = i+1;
            int r = nums.size()-1;
            while(l<r){
                if(nums[i] + nums[l] + nums[r]>0){
                    r--;
                } else if(nums[i] + nums[l] + nums[r]<0){
                    l++;
                } else{
                    vector<int> res = {nums[i], nums[l], nums[r]};
                    ans.push_back(res);
                    l++;
                    r--;
                    while(l<r && nums[l]==nums[l-1]){
                        l++;
                    }
                }
            }
        }
        return ans;
    }
};