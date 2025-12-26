from typing import List
from collections import deque


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        result = []

        # Queue stores entire paths
        queue = deque([[0]])

        while queue:
            path = queue.popleft()
            node = path[-1]

            # If we reached target, save the path
            if node == target:
                result.append(path)
                continue

            # Extend current path with neighbors
            for nei in graph[node]:
                queue.append(path + [nei])

        return result
