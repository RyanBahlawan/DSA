class Solution {
public:
    int countSubstrings(string s) {
        int res = 0;

        for(int i = 0; i<s.size(); i++){
            int l = i, r = i;
            while(l>-1 && r<s.size() && s[l]==s[r]){//odd palindromic substrings
                res++;
                l--;
                r++;
            }

            l = i, r = i + 1;
            while(l>-1 && r<s.size() && s[l]==s[r]){//even palindromic substrings
                res++;
                l--;
                r++;
            }
        }
        return res;
    }
};