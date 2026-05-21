class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort and go through each interval. if theres an overlap, delete the one which 
        # ends later (greedy)

        intervals.sort()
        count = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prevEnd:
                # starts before old interval ends - overlap
                count += 1
                prevEnd = min(end, prevEnd) # update the end value accordingly
                # here we do not delete anything as the problem requires counting
                # choosing the minimum end value reduces probability of later merges
            else:
                prevEnd = end
        return count