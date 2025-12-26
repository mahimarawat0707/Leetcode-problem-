from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0] * n

        # Calculate indegree of each node
        for u, v in edges:
            indegree[v] += 1

        # Nodes with zero indegree must be in the answer
        result = []
        for i in range(n):
            if indegree[i] == 0:
                result.append(i)

        return result
