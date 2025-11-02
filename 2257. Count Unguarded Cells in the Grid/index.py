from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # 0 = empty, 1 = wall, 2 = guard, 3 = guarded
        grid = [[0] * n for _ in range(m)]

        # mark all walls
        for r, c in walls:
            grid[r][c] = 1

        # mark all guards
        for r, c in guards:
            grid[r][c] = 2

        # directions: down, up, right, left
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # sweep from each guard
        for r, c in guards:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                while (
                    0 <= nr < m and 
                    0 <= nc < n and 
                    grid[nr][nc] != 1 and   # stop at wall
                    grid[nr][nc] != 2       # stop at another guard
                ):
                    if grid[nr][nc] == 0:
                        grid[nr][nc] = 3    # mark as guarded
                    nr += dr
                    nc += dc

        # count unguarded cells (value still 0)
        return sum(grid[r][c] == 0 for r in range(m) for c in range(n))
