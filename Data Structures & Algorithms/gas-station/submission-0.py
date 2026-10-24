class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Scan left to right while keeping track of the current tnak balance. If at some index it turns negative, it means that won't work, and reset the total, moving to check from the next station.
        # Complexities: O(n), O(1)
        if sum(gas) < sum(cost):
            return -1

        total = 0
        res = 0

        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                res = i + 1

        return res