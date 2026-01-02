from typing import List
from collections import deque
from operator import itemgetter
from bisect import bisect_right


class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        res = [0] * len(queries)
        idx = []

        # Step 1: Handle easy cases, store hard ones
        for i, q in enumerate(queries):
            a, b = sorted(q)
            if a == b or heights[a] < heights[b]:
                res[i] = b
            else:
                idx.append((a, b, i))

        # Step 2: Process remaining queries using monotonic deque
        j = len(heights) - 1
        mono = deque()

        for a, b, i in sorted(idx, key=itemgetter(1), reverse=True):
            while j > b:
                while mono and heights[mono[0]] < heights[j]:
                    mono.popleft()
                mono.appendleft(j)
                j -= 1

            k = bisect_right(mono, heights[a], key=lambda x: heights[x])
            res[i] = -1 if k == len(mono) else mono[k]

        return res
