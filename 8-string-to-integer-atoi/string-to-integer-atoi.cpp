class Solution {
public:
    int myAtoi(string s) {
        if(s.empty()){
            return 0;
        }
        long long res = 0;
        int sign = 1, i = 0;
        while(i<s.size() && s[i]== ' '){
            i++;
        }
        if(i<s.size() && (s[i]=='-' || s[i]=='+')){
            if(s[i]=='-'){
                sign *= -1;
            }
            i++;
        }
        while(i<s.size() && s[i]=='0'){
            i++;
        }
        while(i<s.size() && s[i]>='0' && s[i]<='9'){
            int digit = s[i]-'0';
            res = res*10+digit;
            if(sign == 1 && res>INT_MAX){
                return INT_MAX;
            } else if(sign == -1 && -1*res<INT_MIN){
                return INT_MIN;
            }
            i++;
        }
        return sign*res;
    }
};