class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        i=0
        
        while i<len(s):
            if s[i] == 'I':
                if (i+1)<len(s) and s[i+1]=='V':
                    digit = 4
                    i+=1
                elif (i+1)<len(s) and s[i+1]=='X':
                    digit = 9
                    i+=1
                else:
                    digit = 1

            elif s[i]=='V':
                digit = 5

            elif s[i] == 'X':
                if (i+1)<len(s) and s[i+1]=='L':
                    digit = 40
                    i+=1
                elif (i+1)<len(s) and s[i+1]=='C':
                    digit = 90
                    i+=1
                else:
                    digit = 10

            elif s[i] == 'L':
                digit = 50

            elif s[i] == 'C':
                if (i+1)<len(s) and s[i+1]=='D':
                    digit = 400
                    i+=1
                elif (i+1)<len(s) and s[i+1]=='M':
                    digit = 900
                    i+=1
                else:
                    digit = 100

            elif s[i]=='D':
                digit = 500
            else:
                digit=1000
            
            res += digit
            i+=1
        return res