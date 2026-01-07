class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> res (temperatures.size(), 0);
        stack<pair<int, int>> s; //{temp, index}

        for(int i = 0; i<temperatures.size(); i++){
            while(!s.empty() && temperatures[i]>s.top().first){
                auto& curr = s.top();
                s.pop();
                res[curr.second] = i-curr.second;

            }
            s.push({temperatures[i], i});
        }
        return res;
    }
};