from typing import List
from collections import defaultdict
from heapq import heappop, heappush
from math import inf


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int]
    ) -> int:

        graph = defaultdict(dict)
        dict_costs = {}

        for u, v, c in zip(original, changed, cost):
            graph[u][v] = min(c, graph[u].get(v, inf))

        def calc_cost(src, tgt):
            if src in dict_costs:
                return dict_costs[src].get(tgt, inf)

            heap = [(0, src)]
            memo = {src: 0}

            while heap:
                cost_current, word = heappop(heap)
                if cost_current == memo[word]:
                    for neighbor, cost_neighbor in graph[word].items():
                        cost_new = cost_current + cost_neighbor
                        if cost_new < memo.get(neighbor, inf):
                            memo[neighbor] = cost_new
                            heappush(heap, (cost_new, neighbor))

            dict_costs[src] = memo
            return memo.get(tgt, inf)

        n = len(source)
        set_len = sorted({len(x) for x in original})

        dp = [inf] * (n + 1)
        dp[0] = 0

        for start in range(n):
            if dp[start] == inf:
                continue

            if source[start] == target[start]:
                dp[start + 1] = min(dp[start + 1], dp[start])

            for l in set_len:
                end = start + l
                if end > n:
                    break

                s = source[start:end]
                if s in graph:
                    dp[end] = min(
                        dp[end],
                        dp[start] + calc_cost(s, target[start:end])
                    )

        return -1 if dp[-1] == inf else dp[-1]
