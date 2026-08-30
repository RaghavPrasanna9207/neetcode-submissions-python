class Solution:
    def hammingWeight(self, n: int) -> int:
        # n = n & (n - 1) removes the rightmost bit. This saves a lot of compute time.
        # Complexities: O(1), O(1)
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count