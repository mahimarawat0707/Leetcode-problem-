from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Initialize distance matrix
        dist = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        # Fill initial edge weights
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        # Floyd–Warshall: all-pairs shortest paths
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        # Find the city with the smallest number of reachable cities
        ans_city = -1
        min_count = float("inf")

        for i in range(n - 1, -1, -1):  # reverse for tie-breaking
            count = 0
            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    count += 1

            if count < min_count:
                min_count = count
                ans_city = i

        return ans_city
