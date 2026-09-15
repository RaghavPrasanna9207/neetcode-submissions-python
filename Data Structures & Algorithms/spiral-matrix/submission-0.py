class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Have four pointers - top, bottom, left and right. While left is lesser than right and top is lesser than bottom, which are the valid conditions, append all the top row elements, then increment top to erase that row. Then append all the right elements, decrement right to erase that row. Do the same with bottom and left. Check validity in the middle, break if it's invalid. This is to prevent duplicates.
        # Complexities: O(m * n), O(1), O(m * n) for the output list.
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break
            
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res