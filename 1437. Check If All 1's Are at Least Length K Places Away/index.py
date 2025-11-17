from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = -1   # index of previous 1

        for i, val in enumerate(nums):
            if val == 1:
                if prev != -1 and (i - prev - 1) < k:
                    return False
                prev = i

        return True
