from typing import List
from collections import defaultdict


class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(set)
        degree = defaultdict(int)

        # Build graph and degree count
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            degree[u] += 1
            degree[v] += 1

        # Collect all nodes with odd degree
        odd_nodes = [node for node in range(1, n + 1) if degree[node] % 2 == 1]

        # Case 1: Already all even
        if len(odd_nodes) == 0:
            return True

        # Case 2: Exactly two odd nodes
        if len(odd_nodes) == 2:
            a, b = odd_nodes

            # Direct edge possible
            if b not in graph[a]:
                return True

            # Try connecting through a third node
            for node in range(1, n + 1):
                if node != a and node != b:
                    if node not in graph[a] and node not in graph[b]:
                        return True

        # Case 3: Exactly four odd nodes
        if len(odd_nodes) == 4:
            a, b, c, d = odd_nodes

            if b not in graph[a] and d not in graph[c]:
                return True
            if c not in graph[a] and d not in graph[b]:
                return True
            if d not in graph[a] and c not in graph[b]:
                return True

        return False
