from typing import List


class UnionFind:
    # Constructor to initialize the Union-Find structure with n elements.
    def __init__(self, n: int):
        # Each element is its own parent initially.
        self.parent = list(range(n))

    # Find function with path compression optimization.
    def find_parent(self, p: int) -> int:
        # If the element is its own parent, return it.
        if self.parent[p] == p:
            return p
        # Otherwise, recursively find the root parent and compress the path.
        self.parent[p] = self.find_parent(self.parent[p])
        return self.parent[p]

    # Union function to merge two sets (u and v).
    def union(self, u: int, v: int) -> None:
        # Find the root parents of u and v.
        pu, pv = self.find_parent(u), self.find_parent(v)
        # Merge them.
        self.parent[pu] = pv


class Solution:
    # Main function to find critical and pseudo-critical edges in a graph.
    def findCriticalAndPseudoCriticalEdges(
        self, n: int, edges: List[List[int]]
    ) -> List[List[int]]:

        critical = []
        pseudo_critical = []

        # Append index to each edge
        for i in range(len(edges)):
            edges[i].append(i)

        # Sort edges by weight
        edges.sort(key=lambda x: x[2])

        # Get MST weight without any restriction
        mst_wt = self.find_mst(n, edges, -1, -1)

        # Check each edge
        for i in range(len(edges)):
            # If removing this edge increases MST weight → critical
            if mst_wt < self.find_mst(n, edges, i, -1):
                critical.append(edges[i][3])
            # If forcing this edge keeps MST same → pseudo-critical
            elif mst_wt == self.find_mst(n, edges, -1, i):
                pseudo_critical.append(edges[i][3])

        return [critical, pseudo_critical]

    # Function to find MST weight, optionally blocking or forcing an edge
    def find_mst(self, n: int, edges: List[List[int]], block: int, e: int) -> int:
        uf = UnionFind(n)
        weight = 0

        # If forcing an edge
        if e != -1:
            weight += edges[e][2]
            uf.union(edges[e][0], edges[e][1])

        # Build MST
        for i in range(len(edges)):
            if i == block:
                continue
            if uf.find_parent(edges[i][0]) == uf.find_parent(edges[i][1]):
                continue
            uf.union(edges[i][0], edges[i][1])
            weight += edges[i][2]

        # Check if graph is fully connected
        for i in range(n):
            if uf.find_parent(i) != uf.find_parent(0):
                return float("inf")

        return weight
