class Solution {
public:
    bool isValid(string s) {
        stack<char> LIFO;
        for(int i = 0; i<s.size(); i++){
            if(s[i]=='(' || s[i]=='[' || s[i]=='{'){
                LIFO.push(s[i]);
            } else{
                if(LIFO.empty()){
                    return false;
                } else if(s[i]==')'){
                    if(LIFO.top()=='('){
                        LIFO.pop();
                    } else{
                        return false;
                    }
                } else if(s[i]=='}'){
                    if(LIFO.top()=='{'){
                        LIFO.pop();
                    } else{
                        return false;
                    }
                } else if(s[i]==']'){
                    if(LIFO.top()=='['){
                        LIFO.pop();
                    } else{
                        return false;
                    }
                }
            }
        }
        if(LIFO.empty()){
            return true;
        } else{
            return false;
        }
    }
};