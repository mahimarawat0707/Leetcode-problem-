from typing import List
from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        tab = defaultdict(set)

        for u, v, w in allowed:
            tab[(u, v)].add(w)

        def add_neighbor(node: str):
            res = ['']
            for i in range(1, len(node)):
                eles = tab[(node[i - 1], node[i])]
                if not eles:
                    return []
                res = [a + e for a in res for e in eles]
            return res

        visited = set()

        def dfs(node: str) -> bool:
            if len(node) == 1:
                return True

            if node in visited:
                return False

            for nxt in add_neighbor(node):
                if dfs(nxt):
                    return True

            visited.add(node)
            return False

        return dfs(bottom)
