class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        orderList = { c:i for i,c in enumerate(order)} #character -> index mapping

        #loop through each word pair
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            #loop through the len of w1 since len(w1) should be <=len(w2)
            for j in range(len(w1)):
                #word 2 is larger than word 1
                if j == len(w2):
                    return False
                if w1[j] != w2[j]:
                    #w1 char comes before w2 char
                    if orderList[w1[j]] < orderList[w2[j]]:
                        break
                    #w1 char comes after w2 char
                    else:
                        return False
        #Everything is in the correct order
        return True