from typing import List

class Solution:
    def maxProfit(
        self,
        n: int,
        present: List[int],
        future: List[int],
        hierarchy: List[List[int]],
        budget: int,
    ) -> int:

        # Build adjacency list
        g = [[] for _ in range(n)]
        for u, v in hierarchy:
            g[u - 1].append(v - 1)

        def dfs(u: int):
            cost = present[u]
            d_cost = present[u] // 2

            # dp[u][state][budget]
            # state 0 → parent NOT purchased
            # state 1 → parent MUST be purchased
            dp0 = [0] * (budget + 1)
            dp1 = [0] * (budget + 1)

            # subProfit[state][budget]
            # state 0 → discount NOT available
            # state 1 → discount available
            sub_profit0 = [0] * (budget + 1)
            sub_profit1 = [0] * (budget + 1)

            u_size = cost

            for v in g[u]:
                child_dp0, child_dp1, v_size = dfs(v)
                u_size += v_size

                for i in range(budget, -1, -1):
                    for sub in range(min(v_size, i) + 1):
                        sub_profit0[i] = max(
                            sub_profit0[i],
                            sub_profit0[i - sub] + child_dp0[sub],
                        )
                        sub_profit1[i] = max(
                            sub_profit1[i],
                            sub_profit1[i - sub] + child_dp1[sub],
                        )

            for i in range(budget + 1):
                dp0[i] = sub_profit0[i]
                dp1[i] = sub_profit0[i]

                if i >= d_cost:
                    dp1[i] = max(
                        dp1[i],
                        sub_profit1[i - d_cost] + future[u] - d_cost,
                    )

                if i >= cost:
                    dp0[i] = max(
                        dp0[i],
                        sub_profit1[i - cost] + future[u] - cost,
                    )

            return dp0, dp1, u_size

        return dfs(0)[0][budget]
