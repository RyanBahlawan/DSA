class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numbers;

        for(int i=0; i<nums.size(); i++){
            int diff = target-nums[i];
            if(numbers.find(diff)!=numbers.end()){
                auto it = numbers.find(diff);
                return {it->second, i};
            } else{
                numbers[nums[i]]=i;
            }
        }
        //error
        return {-1, -1};
    }
};
