class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        length = len(word)
        visit = set()

        def dfs(i, r, c):
            #We found the entire word
            if i == length:
                return True
            
            #Out of bounds, character doesn't match, we already visited that position
            if r>=rows or r<0 or c>=cols or c<0 or word[i]!=board[r][c] or ((r,c) in visit):
                return False
            
            
            #We need to find the rest of the word
            visit.add((r,c))
            res = (dfs(i+1,r-1,c) or dfs(i+1,r,c+1) or dfs(i+1,r+1,c) or dfs(i+1,r,c-1))

            #We remove it from visited since we may need to visit that letter again for other words
            visit.remove((r,c))
            return res

        
        for r in range(rows):
            for c in range(cols):
                if word[0]==board[r][c] and dfs(0,r,c):
                    return True

        return False