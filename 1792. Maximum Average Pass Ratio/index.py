from heapq import heappush, heappop
from typing import List

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(passed, total):
            return (passed + 1) / (total + 1) - passed / total

        heap = []
        for passed, total in classes:
            heappush(heap, (-gain(passed, total), passed, total))

        for _ in range(extraStudents):
            g, passed, total = heappop(heap)
            passed += 1
            total += 1
            heappush(heap, (-gain(passed, total), passed, total))

        total_ratio = 0
        for _, passed, total in heap:
            total_ratio += passed / total

        return total_ratio / len(classes)