class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # To maximise profit, have to choose the lowest buy and highest sell. Keep track of the lowest price and the best profit. At each price, update the maximum profit and the minimum selling price if better ones are found.
        # Complexities: O(n), O(1)
        maxProfit = 0
        minBuy = prices[0]

        for sell in prices:
            maxProfit = max(maxProfit, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxProfit