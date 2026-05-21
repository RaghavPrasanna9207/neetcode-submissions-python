class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start values first
        intervals.sort(key=lambda i : i[0])
        output = [intervals[0]]

        for start, end in intervals:
            # to compare, get the last added value from output
            lastEnd = output[-1][1]

            if start <= lastEnd:
                #compare and merge interval
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])

        return output