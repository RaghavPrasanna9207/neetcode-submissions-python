class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Have a DFS function to mark a cell as 0, and check recursively if it's longer than one cell. Then, have a for loop in the main function to run the DFS fn on any cell which is a 1. We essentially find every island, sink it by turning it into zeros, increment the count and move.
        # Complexities: O(m * n), O(m * n)
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0'):
                return

            grid[r][c] = '0'

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1

        return islands