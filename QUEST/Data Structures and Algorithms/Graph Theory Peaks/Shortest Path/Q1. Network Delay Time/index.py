from typing import List
import heapq
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = defaultdict(list)

        # Build adjacency list
        for u, v, w in times:
            graph[u].append((v, w))

        # Min-heap for Dijkstra
        priority_queue = [(0, K)]
        shortest_path = {}

        while priority_queue:
            curr_time, node = heapq.heappop(priority_queue)

            if node not in shortest_path:
                shortest_path[node] = curr_time

                for neighbor, weight in graph[node]:
                    heapq.heappush(priority_queue, (curr_time + weight, neighbor))

        return max(shortest_path.values()) if len(shortest_path) == N else -1
