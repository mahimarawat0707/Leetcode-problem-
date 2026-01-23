from typing import List
import heapq
from itertools import pairwise


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)

        # Check if already sorted
        if all(x <= y for x, y in pairwise(nums)):
            return 0

        rmv = [False] * n
        prv = [i - 1 for i in range(n)]
        nxt = [i + 1 if i + 1 < n else -1 for i in range(n)]

        heap = [(nums[i] + nums[i + 1], i) for i in range(n - 1)]
        heapq.heapify(heap)

        bad = sum(nums[i] > nums[i + 1] for i in range(n - 1))
        op = 0

        while bad > 0:
            pair_sum, i = heapq.heappop(heap)

            if rmv[i] or nxt[i] == -1:
                continue

            j = nxt[i]
            if rmv[j] or nums[i] + nums[j] != pair_sum:
                continue

            pi = prv[i]
            nj = nxt[j]

            # Remove old violations
            if pi != -1 and nums[pi] > nums[i]:
                bad -= 1
            if nums[i] > nums[j]:
                bad -= 1
            if nj != -1 and nums[j] > nums[nj]:
                bad -= 1

            # Merge
            nums[i] = pair_sum
            rmv[j] = True

            nxt[i] = nj
            if nj != -1:
                prv[nj] = i

            # Add new violations
            if pi != -1 and nums[pi] > nums[i]:
                bad += 1
            if nj != -1 and nums[i] > nums[nj]:
                bad += 1

            # Update heap
            if pi != -1:
                heapq.heappush(heap, (nums[pi] + nums[i], pi))
            if nj != -1:
                heapq.heappush(heap, (nums[i] + nums[nj], i))

            op += 1

        return op
