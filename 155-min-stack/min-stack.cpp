class MinStack {
public:
    stack<long> s;
    long min=0;

    MinStack() {
    }
    
    void push(int val) {
        //push=val-min
        if(s.empty()){
            s.push(0);//push = val-val
            min = val;
        } else{
            long push = val - min;
            s.push(push);
            if(push<0){//update min
                min = val;
            }
        }
    }
    
    void pop() {
        if(s.empty()){
            return;
        }
        long pop = s.top();
        if(pop<0){
            min = min - pop;
        }
        s.pop();
    }
    
    int top() {
        if(s.empty()){
            return -1;
        }
        long top = s.top();
        if(top>0){
            return top+min;
        } else{
            return min;
        }
    }
    
    int getMin() {
        return (int)min;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */