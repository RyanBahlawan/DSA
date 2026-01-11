class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int l = 1, r = 1;
        for(const auto& p : piles){
            r = max(r, p);
        }
        int res = r;

        while(l<=r){
            int k = l+((r-l)/2);
            long long time = 0;
            for(const auto& p : piles){
                time += ceil(static_cast<double>(p)/k);
            }
            if(time<=h){
                res = k;
                r = k - 1;
            } else{
                l = k + 1;
            }
        }
        return res;
    }
};