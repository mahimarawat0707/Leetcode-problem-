from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = sum(nums)
        return total % k
