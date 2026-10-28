class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        #makes the children for the lock
        def children(lock):
            res = []
            #go through each digit
            for i in range(4):
                #incrementing
                digit = str((int(lock[i])+1)%10)
                res.append(lock[:i]+digit+lock[i+1:])
                #decrementing
                digit = str((int(lock[i])-1+10)%10)
                res.append(lock[:i]+digit+lock[i+1:])
            return res

        q = deque()
        q.append(["0000", 0]) #[lock, # of turns]
        visit = set(deadends)
        visit.add("0000")

        while q:
            lock, turns = q.popleft()
            #found the shortest path
            if lock == target:
                return turns

            #add the 8 children
            for child in children(lock):
                #didn't see that lock or not a deadend
                if child not in visit:
                    q.append([child, turns+1])
                    visit.add(child)
        #There is no path
        return -1