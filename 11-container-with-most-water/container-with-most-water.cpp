class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0, r = height.size() - 1, res = 0;
        while(l<=r){
            int h = min(height[l], height[r]);
            int w = r-l;
            res = max(res, w*h);
            if(height[l] >= height[r]){
                r--;
            } else{
                l++;
            }
        }
        return res;
    }
};