class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort() #sorts the first number in the of each list
        res = [intervals[0]]

        for start, end in intervals[1:]:
            #res comes before
            if res[-1][1]<start:
                res.append([start, end])
            
            #overlap
            else:
                interval = [(min(res[-1][0], start)), (max(res[-1][1], end))]
                res.pop()
                res.append(interval)

        return res