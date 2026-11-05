class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        #Each tells us if we found that integer at that index
        t0,t1,t2 = False, False, False

        for triplet in triplets:
            #we skip triplets that have any index value greater than our target
            #we don't want to marge this triplet
            if triplet[0]>target[0] or triplet[1]>target[1] or triplet[2]>target[2]:
                continue
            
            if triplet[0] == target[0]:
                t0 = True
            if triplet[1] == target[1]:
                t1 = True
            if triplet[2] == target[2]:
                t2 = True

        if t0==t1==t2==True:
            return True
        else:
            return False