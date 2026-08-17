class Solution:
    def rob(self, nums: List[int]) -> int:
        # At each step, take a decision to either skip or rob. Take the max and update it to the memo array. Do a DFS, and update the value for each step. Run DFS for the first value to return the answer.
        # Complexities: O(n), O(n)
        memo = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]

            memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return memo[i]

        return dfs(0)