class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size()-1;

        while(l<=r){
            int m = l+((r-l)/2);
            if(nums[m]==target){
                return m;
            }
            if(nums[l]<=nums[m]){ //left half
                if(target<nums[l] || target>nums[m]){ //target is not in range
                    l = m + 1;
                } else{ //target is in range
                    r = m - 1;
                }
            } else{ //right half
                if(nums[m]>target || nums[r]<target){ //target is not in range
                    r = m - 1;
                } else{ //target is in range
                    l = m + 1;
                }
            }
        }
        return -1;
    }
};