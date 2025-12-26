from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        land_cells = 0
        neighbor_pairs = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    land_cells += 1
                    # Check Down neighbor
                    if i < rows - 1 and grid[i + 1][j] == 1:
                        neighbor_pairs += 1
                    # Check Right neighbor
                    if j < cols - 1 and grid[i][j + 1] == 1:
                        neighbor_pairs += 1

        # Each land cell contributes 4, each neighbor pair subtracts 2
        return 4 * land_cells - 2 * neighbor_pairs
