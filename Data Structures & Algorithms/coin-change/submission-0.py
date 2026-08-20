class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Use DFS, go coin wise and update the value with the least amount of coin needed. For each loop, use DFS again for amount - coin recursively to get the value. Take the minimum amount.
        # Complexities: O(n * t), O(t) where n is the length and t is the amount.
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]

            res = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
            memo[amount] = res
            return res

        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins