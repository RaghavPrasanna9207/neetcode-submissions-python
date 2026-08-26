class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Have a dfs, check each letter, then check the next letter across all four directions. Mark it with a hastag before that, so we know not to traverse it. Switch it back after the DFS. Then, DFS for every element in the board.

        # Complexities: O(m * 4^n), O(n) where m is the number of cells in the board, and n is the length of the word.
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or c < 0
            or r >= rows or c >= cols
            or word[i] != board[r][c] or board[r][c] == '#'):
                return False

            board[r][c] = '#'
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            board[r][c] = word[i]
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False