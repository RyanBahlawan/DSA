class Solution {
public:
    int characterReplacement(string s, int k) {
        int result = 0, l = 0, maxF = 0;
        unordered_map<char, int> amount;

        for(int r = 0; r<s.size(); r++){
            amount[s[r]]++;
            maxF = max(maxF, amount[s[r]]);

            while(r-l+1 - maxF > k){
                amount[s[l]]--;
                l++;
            }

            result = max(result, r-l+1);
        }
        return result;
    }
};