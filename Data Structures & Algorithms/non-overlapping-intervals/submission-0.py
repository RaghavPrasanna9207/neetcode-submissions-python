class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort by interval start, if there is a merge, append the count and take the minimum of the current ending and the previous ending, as this greedy method gives us lesser chances of more collisions in the future.
        # Complexities: O(n log n), O(1 or n) depending on the sorting algorithm.
        intervals.sort()
        count = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prevEnd:
                count += 1
                prevEnd = min(end, prevEnd)
            else:
                prevEnd = end
        return count