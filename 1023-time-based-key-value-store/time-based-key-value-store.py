class TimeMap:

    def __init__(self):
        self.map = defaultdict(list) #key -> [[value, time], ..., [value, time]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([value, timestamp])
        return

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.map[key]
        l = 0
        r = len(values)-1

        while l<=r:
            m = (l+r)//2
            if values[m][1]==timestamp:
                return values[m][0]

            elif values[m][1]<timestamp:
                res = values[m][0]
                l=m+1
            #values[m][1]>timestamp
            else:
                r=m-1
        #we return the closest time we have seen to timestamp that is <timestamp
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)