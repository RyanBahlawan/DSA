class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        vector<vector<int>> bucket(nums.size()+1);
        vector<int> res;

        for(const auto& num : nums){
            freq[num]++;
        }

        for(const auto& pair : freq){
            bucket[pair.second].push_back(pair.first);
        }

        for(int i = nums.size(); i>0; i--){
            for(const auto& inner : bucket[i]){
                res.push_back(inner);
                if(res.size()>=k){
                    return res;
                }
            }
        }
        return res;

    }
};
