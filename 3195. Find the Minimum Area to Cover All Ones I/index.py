from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        """
        Find the smallest rectangle that covers all the 1's in the grid.
        Returns the area of that rectangle.
        """
        m, n = len(grid), len(grid[0])   # Dimensions: rows (m) and columns (n)

        # Initialize rectangle boundaries
        top, bottom = m, -1
        left, right = n, -1

        # Scan the grid to find the extreme positions of 1's
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    top = min(top, i)
                    bottom = max(bottom, i)
                    left = min(left, j)
                    right = max(right, j)

        # If no 1's found, area is 0
        if bottom == -1:
            return 0

        # Area = height * width
        height = bottom - top + 1
        width = right - left + 1

        return height * width

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
    ]

    solution = Solution()
    print(solution.minimumArea(grid))  # Output: 4
