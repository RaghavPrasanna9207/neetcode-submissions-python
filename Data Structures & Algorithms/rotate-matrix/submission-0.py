class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Use a while loop to rotate layer by layer. Inside the while loo, use a for loop to rotate each set of elements. Increment and decrement i in the necessary places. (r - l) tells us how many cells are there in each row of the current layer.
        # Complexities: O(n^2), O(1)
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                topLeft = matrix[top][l + i]
                matrix[top][l + i] = matrix[bottom - i][l]
                matrix[bottom - i][l] = matrix[bottom][r - i]
                matrix[bottom][r - i] = matrix[top + i][r]
                matrix[top + i][r] = topLeft
            r -= 1
            l += 1