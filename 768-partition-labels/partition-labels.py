class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        lastIndexChar = defaultdict(int)

        for i in range(len(s)):
            lastIndexChar[s[i]] = max(lastIndexChar[s[i]], i)

        size = 0
        end = 0
        groups = []
        
        for i in range(len(s)):
            end = max(lastIndexChar[s[i]], end)
            size+=1

            if i==end:
                groups.append(size)
                size = 0
        return groups