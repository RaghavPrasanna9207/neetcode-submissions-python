"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Here, we can use two pointers, one to check the meeting start times, and one to check the end times. Have two sorted arrays, and compare. If a meeting starts before another ends, we need a new room. Append count and move the s pointer forward. If not, decrement the count and move the e pointer forward. After each iteration, update the max value of the count.
        # Complexities: O(n log n), O(n)
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res = count = 0
        s = e = 0
        
        while s < len(intervals):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)
        return res