class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []
        #small is a maxheap, large is a minheap

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:#push to large heap if num greater than min of large
            heapq.heappush(self.large, num) 
        else: #else push to small
            heapq.heappush(self.small, -1 * num)

        #balancing heaps
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
        
        return (-1 * self.small[0] + self.large[0]) / 2