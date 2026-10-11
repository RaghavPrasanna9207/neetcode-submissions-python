class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Use max heap, take the two, smash them, if there's a difference, push it. Return either zero or the weight of the remaining stone.
        # Complexities: O(n log n), O(n)
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])