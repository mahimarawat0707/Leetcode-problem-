from typing import List

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # Create a (n+1) x (n+1) difference matrix
        diff = [[0] * (n + 1) for _ in range(n + 1)]
        
        # Apply range updates
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1
            diff[r2 + 1][c2 + 1] += 1
        
        # Prefix sum horizontally
        for i in range(n):
            for j in range(1, n):
                diff[i][j] += diff[i][j - 1]
        
        # Prefix sum vertically
        for j in range(n):
            for i in range(1, n):
                diff[i][j] += diff[i - 1][j]
        
        # Extract the n x n result grid
        return [row[:n] for row in diff[:n]]
