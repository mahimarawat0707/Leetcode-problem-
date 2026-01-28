from collections import defaultdict
from typing import List


class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        """
        dp[i][j] = minimum cost to reach cell (i, j)

        When k = 0:
        dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        """

        m, n = len(grid), len(grid[0])

        # Build teleportation map
        teleport = defaultdict(list)
        for i in range(m):
            for j in range(n):
                teleport[grid[i][j]].append((i, j))

        inf = float("inf")
        dp = [[inf] * n for _ in range(m)]
        dp[0][0] = 0

        def update_dp():
            for i in range(m):
                for j in range(n):
                    cost = grid[i][j] + min(
                        dp[i - 1][j] if i > 0 else inf,
                        dp[i][j - 1] if j > 0 else inf,
                    )
                    dp[i][j] = min(dp[i][j], cost)

        # Initial DP (k = 0)
        update_dp()

        # Apply teleportation k times
        keys = sorted(teleport.keys(), reverse=True)

        for _ in range(k):
            best = inf
            for key in keys:
                for i, j in teleport[key]:
                    best = min(best, dp[i][j])
                for i, j in teleport[key]:
                    dp[i][j] = best
            update_dp()

        return dp[-1][-1]
