class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort() #sorts the array based on the first index

        res = 0 #counts the amount of intervals we delete
        prevEnd = intervals[0][1] #stores the previous end

        for start, end in intervals[1:]:
            #first ends before second start
            if prevEnd<=start:
                prevEnd = end
            
            #overlap
            else:
                res+=1
                #we are deleting the longest interval, thus we keep the interval with the smallest end
                prevEnd = min(end, prevEnd)
        return res