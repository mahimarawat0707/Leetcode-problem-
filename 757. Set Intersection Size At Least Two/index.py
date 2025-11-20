from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort: by end asc, and when tie, start desc
        intervals.sort(key=lambda x: (x[1], -x[0]))

        # The last two selected points
        a = -1
        b = -1
        res = 0

        for s, e in intervals:
            # Case 1: both a and b already inside interval
            if s <= a and s <= b:
                continue

            # Case 2: only b is inside interval (need 1 more)
            if s > a and s <= b:
                res += 1
                a = b
                b = e
            else:
                # Case 3: none inside interval (need 2)
                res += 2
                a = e - 1
                b = e
        
        return res
