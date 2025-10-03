import heapq
from typing import List

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []
        
        # Push all boundary cells into heap
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        trapped_water = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        max_height = 0
        
        while heap:
            height, x, y = heapq.heappop(heap)
            max_height = max(max_height, height)
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if heightMap[nx][ny] < max_height:
                        trapped_water += max_height - heightMap[nx][ny]
                    heapq.heappush(heap, (heightMap[nx][ny], nx, ny))
        
        return trapped_water


# ---------------- Test in VS Code ----------------
if __name__ == "__main__":
    sol = Solution()
    
    heightMap1 = [[1,4,3,1,3,2],
                  [3,2,1,3,2,4],
                  [2,3,3,2,3,1]]
    print("Example 1 Output:", sol.trapRainWater(heightMap1))  # Expected 4
    
    heightMap2 = [[3,3,3,3,3],
                  [3,2,2,2,3],
                  [3,2,1,2,3],
                  [3,2,2,2,3],
                  [3,3,3,3,3]]
    print("Example 2 Output:", sol.trapRainWater(heightMap2))  # Expected 10