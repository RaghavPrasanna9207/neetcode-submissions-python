class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Use binary search, calculate row and col using m, which is calculated each iteration.
        # Complexities: O(log(m * n)), O(1)
        rows, cols = len(matrix), len(matrix[0])

        l, r = 0, rows * cols - 1
        while l <= r:
            m = (l + r) // 2
            row = m // cols
            col = m % cols

            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True

        return False