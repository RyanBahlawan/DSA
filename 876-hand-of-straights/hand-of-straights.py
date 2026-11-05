class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        #not divisible by groupSize
        if (len(hand)%groupSize) != 0:
            return False

        total = len(hand)//groupSize #gives us the expected amount of groups
        res=0 #the amount of groups we made

        hand.sort()
        count = defaultdict(int)

        #create the count hashmap
        for n in hand:
            count[n]+=1

        #go through each number
        for n in hand:
            start = n
            #make sure we are at the start of a sequence
            while start-1 in count and count[start-1]>0:
                start-=1

            #already used that number
            if count[start]==0:
                continue

            #create the group
            for i in range(start, start+groupSize):
                if count[i]:
                    count[i]-=1
                else:
                    return False
            res+=1

        if res==total:
            return True
        else:
            return False