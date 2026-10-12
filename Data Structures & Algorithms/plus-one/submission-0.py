class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Go right to left, if it's a 9, set it to zero. If the loop ends, return [1] + digits as it means that all digits were 9.
        # Complexities: O(n), O(n)
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits