from typing import List
from functools import cache


class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)

        @cache
        def dfs(i: int, j: int, state: int) -> int:
            # j = remaining transactions
            # state:
            # 0 -> no stock in hand
            # 1 -> holding stock (buy)
            # 2 -> just sold stock

            if j == 0:
                return 0

            if i == 0:
                if state == 0:
                    return 0
                elif state == 1:
                    return -prices[0]
                else:
                    return prices[0]

            price = prices[i]

            if state == 0:
                res = max(
                    dfs(i - 1, j, 0),          # do nothing
                    dfs(i - 1, j, 1) + price, # sell
                    dfs(i - 1, j, 2) - price  # buy again
                )

            elif state == 1:
                res = max(
                    dfs(i - 1, j, 1),          # keep holding
                    dfs(i - 1, j - 1, 0) - price  # buy
                )

            else:  # state == 2
                res = max(
                    dfs(i - 1, j, 2),          # cooldown
                    dfs(i - 1, j - 1, 0) + price  # sell
                )

            return res

        ans = dfs(n - 1, k, 0)
        dfs.cache_clear()
        return ans
