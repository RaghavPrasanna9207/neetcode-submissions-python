"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # this can be done using two pointers - for start and end time
        # going thru these timelines in order, we calculate number of rooms
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res = count = 0
        s = e = 0

        while s < len(intervals):
            if start[s] < end[e]:
                # meeting started before earlier meeting ended
                s += 1
                count += 1
            else:
                # meeting ended
                e += 1
                count -= 1
            res = max(count, res) # calc res after each iteration
        return res