from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        # Manhattan distance between two points
        def cost(p1: List[int], p2: List[int]) -> int:
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        min_cost = 0  # Total cost of the Minimum Spanning Tree (MST)

        # Track minimum distance of each node not yet in MST
        adj = {i: float('inf') for i in range(len(points))}
        adj[0] = 0  # Start MST from node 0

        # Prim’s Algorithm
        while adj:
            # Pick node with smallest edge cost
            i, c = min(adj.items(), key=lambda item: item[1])
            min_cost += c
            node = points[i]
            del adj[i]  # Add node to MST

            # Update costs of remaining nodes
            for k in adj:
                new_cost = cost(node, points[k])
                if new_cost < adj[k]:
                    adj[k] = new_cost

        return min_cost
