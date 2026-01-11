class Solution {
public:
    int findMin(vector<int>& nums) {
        int l = 0, r = nums.size()-1, res = nums[0];
        while(l<=r){
            int m = l + ((r-l)/2);
            if(nums[m]>=nums[l]){ // search right
                res = min(res, nums[l]);
                l = m + 1;
            } else{ //search left
                res = min(res, nums[m]);
                r = m - 1;
            }
        }
        return res;
    }
};