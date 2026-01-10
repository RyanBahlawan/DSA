class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        if(strs.size() == 0){
            return {{""}};
        }

        unordered_map<string, vector<string>> anagrams;

        //go through each string in the vector
        for(const auto& s : strs){
            //create a vector of 26 elements for each letter
            vector<char> alphabets (26, 0); //create a vector of size 26 with each element having a value of 0
            //go through each letter in the string
            for(const auto& c : s){
                alphabets[c - 'a']++; //increment the specific letter
            }

            //convert back alphabets vector back to string
            string word = to_string(alphabets[0]);
            for(int i = 1; i<26; ++i){
                word += ',' + to_string(alphabets[i]);
            }

            anagrams[word].push_back(s);

        }

        //go through each key in the list and store in a vector
        vector<vector<string>> list;
        for(const auto& pair : anagrams){
            list.push_back(pair.second);
        }
        return list;

    }
};