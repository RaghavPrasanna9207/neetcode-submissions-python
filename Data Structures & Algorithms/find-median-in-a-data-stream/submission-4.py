class MedianFinder:
    # To find the median efficiently, we will use two heaps, small the maxheap and large the minheap. If one of them is greater in size compared to the other, then pick the border element closer to the middle, as that is the median. If not, take the two border elements and get their average. To add a number, add it to large if the number is greater than the smallest number of large. If not, add it to small. Make sure to check and rebalance the heaps, the maximum size difference can only be 1. Since python only has min heaps, max heaps can be implemented by multiplying everything with -1.
    # Complexities: O(m * log n) for addNum(), O(m) for findMedian(), O(n)
    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return ((-1 * self.small[0]) + self.large[0]) / 2