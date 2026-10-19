class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1)<len(nums2):
            temp = nums2
            nums2 = nums1
            nums1=temp

        total = len(nums1)+len(nums2)
        half = total//2

        l = 0
        r = len(nums2)-1
        #nums2 is the smaller array
        #A is nums2, B is nums1
        while True:
            midA = (l+r)//2
            midB = half-midA-2

            if midA>=0:
                leftA=nums2[midA]
            else:
                leftA=float("-infinity")

            if midA+1<len(nums2):
                rightA=nums2[midA+1]
            else:
                rightA=float("infinity")

            if midB>=0:
                leftB=nums1[midB]
            else:
                leftB=float("-infinity")

            if midB+1<len(nums1):
                rightB=nums1[midB+1]
            else:
                rightB=float("infinity")

            #we have found the middle
            if (leftA<=rightB and leftB<=rightA):
                #Odd
                if total%2==1:
                    return min(rightA,rightB)

                #Even
                else:
                    return (max(leftA,leftB) + min(rightA,rightB))/2

            #nums2 has a larger number in the left portion than nums1's right portion
            elif leftA>rightB:
                r = midA-1
            
            #leftB>rightA; meaning nums1 has a larger number in the left portion than the right portion
            else:
                l=midA+1