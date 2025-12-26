class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> res;

        for(int i = 0; i<intervals.size(); i++){
            if(newInterval[1]<intervals[i][0]){//newInterval comes before an interval
                res.push_back(newInterval);
                copy(intervals.begin() + i, intervals.end(), back_inserter(res));//copies the rest of the intervals into res
                return res;
            } else if(newInterval[0]>intervals[i][1]){//newInterval comes after an interval
                res.push_back(intervals[i]);
            } else{ //interval overlap
                newInterval[0] = min(newInterval[0], intervals[i][0]);
                newInterval[1] = max(newInterval[1], intervals[i][1]);
            }
        }
        res.push_back(newInterval);//insert the newInterval
        return res;
    }
};