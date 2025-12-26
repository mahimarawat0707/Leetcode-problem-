from typing import List
from collections import defaultdict


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        complete_count = 0

        def dfs(node: int, component: set):
            component.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor, component)

        for i in range(n):
            if i not in visited:
                component = set()
                visited.add(i)
                dfs(i, component)
                
                # Check if every node has exactly len(component)-1 neighbors
                if all(len(adj[node]) == len(component) - 1 for node in component):
                    complete_count += 1

        return complete_count
