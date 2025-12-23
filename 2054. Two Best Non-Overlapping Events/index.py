from typing import List
from collections import deque
from operator import itemgetter


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Sort events by end time
        end_sorted = deque(sorted(events, key=itemgetter(1)))
        
        # Sort events by start time
        start_sorted = sorted(events, key=itemgetter(0))

        # At least one event can always be chosen
        ans = max(value for _, _, value in events)

        end_max = 0

        for start, end, value in start_sorted:
            # Remove events that end before the current event starts
            while end_sorted and end_sorted[0][1] < start:
                _, _, v = end_sorted.popleft()
                end_max = max(end_max, v)

            # Update the answer with best non-overlapping combination
            ans = max(ans, value + end_max)

        return ans
