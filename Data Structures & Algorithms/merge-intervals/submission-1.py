class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Have a result array and add the first interval to it. Sort the intervals array. Iterate through the array, and check if each interval is overlapping. If so, merge them. Check by checking the current interval's start and the previously added interval's end. If there is an overlap, merge them. Otherwise, append to the result array.
        # Complexities: O(n log n), O(1 or n) for extra space(based on sorting), O(n) for the output list.
        intervals.sort(key = lambda i: i[0])
        result = [intervals[0]]

        for start, end in intervals:
            lastEnd = result[-1][-1]

            if start <= lastEnd:
                result[-1][-1] = max(lastEnd, end)
            else:
                result.append([start, end])

        return result