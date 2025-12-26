class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l = 0, result = 0;
        unordered_set<char> window;

        for(int r = 0; r<s.size(); r++){
            while(window.find(s[r])!=window.end()){
                window.erase(s[l]);
                l++;
            }
            window.insert(s[r]);
            result = max(result, r-l+1);
        }
        return result;
    }
};