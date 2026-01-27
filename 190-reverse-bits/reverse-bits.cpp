class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        int res = 0;

        for(int i = 0; i<32; i++){
            int bit = (n >>i) & 1; //get the first bit on the ith iteration
            res = res | (bit<<(31-i)); //store it at the ith last bit
        }
        return res;
    }
};
