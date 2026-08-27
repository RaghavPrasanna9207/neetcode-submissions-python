class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Three cases: 1. If the new interval occurs before the current interval, append that to the result and return the result + everything that follows from intervals. 2. If the new interval is after the current interval, append the current interval to the result. If there is an overlap, expand by picking the minimum and maximum of both to converge them properly.
        # Complexities: O(n), O(1) extra space, O(n) for output list.
        
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        res.append(newInterval)
        return res