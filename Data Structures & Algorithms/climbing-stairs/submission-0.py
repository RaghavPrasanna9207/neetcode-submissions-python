class Solution:
    def climbStairs(self, n: int) -> int:
        # In order to reach a step, you have to ways: from the step before, and the one before that. This repeats for all steps. So if you take the sum of ways to reach the previous step, and the one before that, that will give you the number of ways to reach the current step.
        # Complexities: O(n), O(n)
        if n < 3:
            return n

        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]