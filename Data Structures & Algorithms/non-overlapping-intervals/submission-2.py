class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort the array, take the first interval's end. From there, check if the next interval's start is lesser. If so, increment the count. After every check, update the end value that is checked to the minimum of the current value and the current interval's end value. Taking the minimum leaves less space for more overlaps in the future, and this is the Greedy part of the algorithm.
        # Complexities: O(n log n), O(1 or n) depending on sort.

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