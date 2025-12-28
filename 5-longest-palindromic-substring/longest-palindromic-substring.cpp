class Solution {
public:
    string longestPalindrome(string s) {
        int resLen = 0;
        pair<int, int> res = {-1, -1};
        
        for(int i = 0; i<s.size(); i++){
            int l = i, r = i;

            while(l>-1 && r<s.size() && s[l]==s[r]){
                if((r-l+1)>resLen){
                    resLen = r-l+1;
                    res = {l, r};
                }
                l--;
                r++;
            }

            l = i, r = i+1;

            while(l>-1 && r<s.size() && s[l]==s[r]){
                if((r-l+1)>resLen){
                    resLen = r-l+1;
                    res = {l, r};
                }
                l--;
                r++;
            }
            

        }

        if(resLen == 0){
            return "";
        } else{
            return s.substr(res.first, resLen);
        }
    }
};