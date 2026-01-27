from typing import List
from itertools import accumulate


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])

        # Prefix sums for rows
        rowSum = [list(accumulate(row, initial=0)) for row in grid]

        # Prefix sums for columns (using transpose trick)
        colSum = [list(accumulate(col, initial=0)) for col in zip(*grid)]

        # Prefix sums for diagonals
        diag = [[0] * (c + 1) for _ in range(r + 1)]
        antidiag = [[0] * (c + 1) for _ in range(r + 1)]

        for i in range(r):
            for j in range(c):
                diag[i + 1][j + 1] = diag[i][j] + grid[i][j]
                antidiag[i + 1][j] = antidiag[i][j + 1] + grid[i][j]

        def isMagic(k: int) -> bool:
            for i in range(r - k + 1):
                for j in range(c - k + 1):
                    total = diag[i + k][j + k] - diag[i][j]
                    anti = antidiag[i + k][j] - antidiag[i][j + k]

                    if total != anti:
                        continue

                    for m in range(k):
                        if (
                            total != rowSum[i + m][j + k] - rowSum[i + m][j]
                            or total != colSum[j + m][i + k] - colSum[j + m][i]
                        ):
                            break
                    else:
                        return True
            return False

        for k in range(min(r, c), 1, -1):
            if isMagic(k):
                return k

        return 1
