from typing import List
import bisect

class SummaryRanges:

    def __init__(self):
        self.intervals = []   # list of [start, end]

    def addNum(self, value: int) -> None:
        newInterval = [value, value]
        intervals = self.intervals

        # Find the position to insert the new interval
        i = bisect.bisect_left(intervals, newInterval)

        # Merge with left interval if possible
        if i > 0 and intervals[i - 1][1] + 1 >= value:
            i -= 1

        # Start merging process
        start, end = value, value

        while i < len(intervals) and intervals[i][0] <= end + 1:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            intervals.pop(i)

        intervals.insert(i, [start, end])

    def getIntervals(self) -> List[List[int]]:
        return self.intervals[:]
