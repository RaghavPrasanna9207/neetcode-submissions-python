class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Have an array DP, where each element represents the LAS from that element. (DP[3] gives the LAS length starting from index 3). Have a for loop to check what characters to include, and including them if they are greater.
        # Complexities: O(n^2), O(n)

        n = len(nums)
        dp = [-1] * n

        def dfs(i):
            if dp[i] != -1:
                return dp[i]

            lis = 1
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    lis = max(lis, 1 + dfs(j))

            dp[i] = lis
            return lis
        return max(dfs(i) for i in range(n))