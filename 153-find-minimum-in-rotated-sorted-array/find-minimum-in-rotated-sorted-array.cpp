class Solution {
public:
    int findMin(vector<int>& nums) {
        int l = 0, r = nums.size()-1, res = nums[0];
        while(l<=r){
            int m = l + ((r-l)/2);
            if(nums[m]>=nums[l]){ //check left half
                res = min(res, nums[l]); //check left most and res for min value
                l = m + 1; //search right
            } else{ //check right half
                res = min(res, nums[m]); //check left most value (middle in this case) and res for min value
                r = m - 1; //search left half
            }
        }
        return res;
    }
};