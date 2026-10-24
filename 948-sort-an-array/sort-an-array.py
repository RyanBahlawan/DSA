class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, l, m, r):
            left = arr[l:m+1]
            right = arr[m+1:r+1]
            i = l
            lA = 0
            rA = 0

            while lA<len(left) and rA<len(right):
                if left[lA]<=right[rA]:
                    nums[i] = left[lA]
                    lA+=1
                else:
                    nums[i] = right[rA]
                    rA+=1
                i+=1
            
            while lA<len(left):
                nums[i] = left[lA]
                lA+=1
                i+=1

            while rA<len(right):
                nums[i] = right[rA]
                rA+=1
                i+=1
        
        def mergeSort(arr, l, r):
            if l>=r:
                return

            m = (l+r)//2
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)
            merge(arr, l, m, r)
        
        mergeSort(nums, 0, len(nums)-1)
        return nums