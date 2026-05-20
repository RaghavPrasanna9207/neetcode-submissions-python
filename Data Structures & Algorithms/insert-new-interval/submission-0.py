class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):

            #new interval comes before
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            #comes after
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
                #each interval gets appended so that result becomes intervals

            #overlapping intervals
            else:
                #combine lower limit and upper limit
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
        
        res.append(newInterval)
        return res