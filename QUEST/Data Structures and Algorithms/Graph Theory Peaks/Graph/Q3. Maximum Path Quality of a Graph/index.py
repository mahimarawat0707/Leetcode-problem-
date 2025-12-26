from typing import List
from collections import defaultdict


class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        graph = defaultdict(list)

        # Build graph
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        self.best = 0

        def dfs(node: int, time_left: int, quality: int, visited_mask: int):
            # Every time we return to node 0, try updating answer
            if node == 0:
                self.best = max(self.best, quality)

            for nxt, cost in graph[node]:
                if cost > time_left:
                    continue

                # If nxt not visited yet, gain its value
                if not (visited_mask & (1 << nxt)):
                    dfs(
                        nxt,
                        time_left - cost,
                        quality + values[nxt],
                        visited_mask | (1 << nxt)
                    )
                else:
                    dfs(
                        nxt,
                        time_left - cost,
                        quality,
                        visited_mask
                    )

        # Start from node 0
        dfs(0, maxTime, values[0], 1)

        return self.best
