from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_mod = sum(nums) % p
        if total_mod == 0:
            return 0

        prefix_mod = 0
        seen = {0: -1}
        res = len(nums)

        for i, num in enumerate(nums):
            prefix_mod = (prefix_mod + num) % p
            target = (prefix_mod - total_mod) % p

            if target in seen:
                res = min(res, i - seen[target])

            seen[prefix_mod] = i

        return res if res < len(nums) else -1
