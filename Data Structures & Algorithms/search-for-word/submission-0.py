class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (min(r, c) < 0 or #not out of bounds
            r >= rows or c >= cols or
            word[i] != board[r][c] or #not equal
            (r, c) in path): #alr exists
                return False

            path.add((r, c))
            res = (dfs(r + 1, c, i +1) or #continue in all 4 dir
                dfs(r - 1, c, i +1) or
                dfs(r, c + 1, i +1) or
                dfs(r, c - 1, i +1))

            path.remove((r, c))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): #check everything
                    return True
        return False