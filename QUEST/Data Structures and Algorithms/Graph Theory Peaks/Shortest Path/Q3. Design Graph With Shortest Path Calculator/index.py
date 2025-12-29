from typing import List
import heapq


class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        """
        Initialize the graph with 'n' nodes and a list of weighted edges.
        """
        self.nodes = n
        self.graph = {i: {} for i in range(n)}

        for u, v, w in edges:
            self.graph[u][v] = w

    def addEdge(self, edge: List[int]) -> None:
        """
        Add a directed edge (u -> v) with weight w.
        """
        u, v, w = edge
        self.graph[u][v] = w

    def shortestPath(self, node1: int, node2: int) -> int:
        """
        Return the minimum cost from node1 to node2 using Dijkstra.
        If no path exists, return -1.
        """
        INF = float("inf")
        dist = [INF] * self.nodes
        dist[node1] = 0

        pq = [(0, node1)]  # (distance, node)

        while pq:
            curr_dist, node = heapq.heappop(pq)
            if curr_dist > dist[node]:
                continue

            for nei, w in self.graph[node].items():
                new_dist = curr_dist + w
                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    heapq.heappush(pq, (new_dist, nei))

        return dist[node2] if dist[node2] != INF else -1
