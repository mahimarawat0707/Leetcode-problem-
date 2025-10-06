import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        min_heap = [(grid[0][0], 0, 0)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited[0][0] = True
        res = 0

        while min_heap:
            time, x, y = heapq.heappop(min_heap)
            res = max(res, time)

            if x == n - 1 and y == n - 1:
                return res

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    heapq.heappush(min_heap, (grid[nx][ny], nx, ny))

        return res
