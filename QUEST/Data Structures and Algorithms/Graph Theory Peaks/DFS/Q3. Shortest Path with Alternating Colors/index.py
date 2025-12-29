from typing import List
from collections import defaultdict, deque


class Solution:
    def shortestAlternatingPaths(
        self,
        n: int,
        redEdges: List[List[int]],
        blueEdges: List[List[int]]
    ) -> List[int]:

        graph = defaultdict(list)

        # Build graph with edge colors
        for u, v in redEdges:
            graph[u].append((v, "r"))
        for u, v in blueEdges:
            graph[u].append((v, "b"))

        ans = [-1] * n
        queue = deque([(0, 0, None)])   # (node, distance, previous edge color)
        visited = set()

        while queue:
            node, dist, prev_edge = queue.popleft()
            visited.add((node, prev_edge))

            if ans[node] == -1:
                ans[node] = dist

            for neighbor, edge_color in graph[node]:
                if (neighbor, edge_color) not in visited and prev_edge != edge_color:
                    queue.append((neighbor, dist + 1, edge_color))

        return ans
