class Solution {
public:
    string minWindow(string s, string t) {
        if(t.empty()){
            return "";
        }

        unordered_map<char, int> window, countT;

        //create the frequency for t
        for(char c : t){
            countT[c]++;
        }

        int have = 0, need = countT.size();
        pair<int, int> res = {-1, -1};
        int resLen = INT_MAX, l = 0;

        //make the window
        for(int r = 0; r<s.size(); r++){
            window[s[r]]++;

            //found a character in s that is in t and frequencies match
            if(countT.find(s[r]) != countT.end() && window[s[r]]==countT[s[r]]){
                have++;
            }

            //make window smaller
            while(have == need){

                //update the minimum window
                if(r-l+1<resLen){
                    resLen = r-l+1;
                    res = {l, r};
                }

                window[s[l]]--;

                //we removed a manadatory cahracter
                if(countT.find(s[l]) != countT.end() && window[s[l]]<countT[s[l]]){
                    have--;
                }
                l++;
            }
        }

        if(resLen == INT_MAX){
            return "";
        } else{
            return s.substr(res.first, resLen);
        }
    }
};