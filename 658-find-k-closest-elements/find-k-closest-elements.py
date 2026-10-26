class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #m is our starting index value for our window. This algorithm looks for the best starting window.
        #At each iteration we split the total possible amount of starting windows by half.
        #Once we find the best starting window we return the window
        l = 0
        r = len(arr)-k

        while l<r:
            m = (l+r)//2
            left = abs(x-arr[m])
            right = abs(x-arr[m+k])

            #if left>right that means the left element is farther than the right element, l=m+1
            #if (left==right and arr[m+k]<x) means that the left and right elements are equal but the
            # right element is less than our target, so l=m+1
            if (left > right) or (left==right and arr[m+k]<x):
                l = m+1
            
            #if left < right
            #if left==right
            else:
                r = m
        return arr[l:l+k]