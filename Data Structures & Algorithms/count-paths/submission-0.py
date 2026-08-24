class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # The entire bottom row will be all 1s, because they can only go right. Any cell above that row will be the sum of the cell below it, and the cell to its right, as it can go there. Here we have two rows alone, as we don't need all that extra space. Let row be the last row, newRow the second last, and keep updating and return the first cell.
        # Complexities: O(m * n), O(n)
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]