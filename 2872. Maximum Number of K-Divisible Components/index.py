from typing import List
from collections import defaultdict

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = defaultdict(list)

        # Build the adjacency list
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        count = 0

        def dfs(node):
            nonlocal count
            visited[node] = True
            subtotal = values[node]

            for nei in graph[node]:
                if not visited[nei]:
                    subtotal += dfs(nei)

            if subtotal % k == 0:
                count += 1
                return 0  # this component is divisible and considered "clean"
            
            return subtotal

        dfs(0)
        return count
