class Solution:
    def countBits(self, n: int) -> List[int]:
        # Numbers repeat their bit patterns every time we reach a power of two. (0, 1, 10, 11, 100) - we can see that to go from 3 to 7, we go from 11 to 111. So we take the offset(or the power of 2), check the previous iteration of that and add 1 to it. 
        # Complexities: O(n), O(1) extra space, O(n) space for output array.
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = dp[i - offset] + 1
        return dp