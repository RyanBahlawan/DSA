class Solution:
    def partition(self, s: str) -> list[list[str]]:
        #We are partitioning the string and checking if that partion is a palindrome. If it is then we continue to check if the j+1 portion is a palindrome. The base case is when we reached the end of the string, thus this is a valid palindrom partition.
        #At every decision we are deciding whether to partion it or not.

        def isPalindrome(i,j):
            l = i
            r = j
            while l<r:
                if s[l]!=s[r]:
                    return False
                else:
                    l+=1
                    r-=1
            return True

        res = []
        part = []
        def backtrack(i):
            if i == len(s):
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):
                if isPalindrome(i,j):
                    part.append(s[i:j+1])
                    backtrack(j+1)
                    part.pop()

        backtrack(0)
        return res