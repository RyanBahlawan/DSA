class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)

        #pattern->word
        adj = defaultdict(list)
        #Build the adjacency list
        for w in wordList:
            for j in range(len(w)):
                pattern = w[:j]+"*"+w[j+1:]
                adj[pattern].append(w)

        def bfs(word):
            visit = set()
            q = deque()
            q.append(word)
            visit.add(word)
            res = 1

            while q:
                level = len(q)
                for i in range(level):
                    curWord = q.popleft()
                    if curWord == endWord:
                        return res
                    for j in range(len(curWord)):
                        pattern = curWord[:j]+"*"+curWord[j+1:]
                        for word in adj[pattern]:
                            if word not in visit:
                                q.append(word)
                                visit.add(word)
                res+=1
            return 0


        return bfs(beginWord)