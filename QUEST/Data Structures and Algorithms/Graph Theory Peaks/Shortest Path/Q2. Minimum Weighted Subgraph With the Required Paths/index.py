from typing import List
from collections import defaultdict
import heapq


class Solution:
    def minimumWeight(
        self,
        n: int,
        edges: List[List[int]],
        src1: int,
        src2: int,
        dest: int
    ) -> int:

        graph = defaultdict(list)
        rev_graph = defaultdict(list)

        # Build normal and reversed graphs
        for u, v, w in edges:
            graph[u].append((v, w))
            rev_graph[v].append((u, w))

        def dijkstra(start: int, g):
            dist = [float('inf')] * n
            dist[start] = 0
            pq = [(0, start)]  # (distance, node)

            while pq:
                curr_dist, node = heapq.heappop(pq)
                if curr_dist > dist[node]:
                    continue

                for nei, w in g[node]:
                    new_dist = curr_dist + w
                    if new_dist < dist[nei]:
                        dist[nei] = new_dist
                        heapq.heappush(pq, (new_dist, nei))

            return dist

        dist1 = dijkstra(src1, graph)
        dist2 = dijkstra(src2, graph)
        dist3 = dijkstra(dest, rev_graph)

        ans = float('inf')
        for i in range(n):
            if dist1[i] != float('inf') and dist2[i] != float('inf') and dist3[i] != float('inf'):
                ans = min(ans, dist1[i] + dist2[i] + dist3[i])

        return ans if ans != float('inf') else -1
