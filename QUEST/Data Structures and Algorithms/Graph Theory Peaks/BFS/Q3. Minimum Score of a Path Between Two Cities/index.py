from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Build adjacency list: graph[node] = list of (neighbor, weight)
        graph = [[] for _ in range(n + 1)]
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        visited = [False] * (n + 1)
        min_edge = float('inf')

        def dfs(node: int):
            nonlocal min_edge
            visited[node] = True
            for neighbor, weight in graph[node]:
                min_edge = min(min_edge, weight)
                if not visited[neighbor]:
                    dfs(neighbor)

        # Start DFS from node 1
        dfs(1)

        return min_edge
