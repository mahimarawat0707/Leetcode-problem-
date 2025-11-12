from math import gcd
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)

        if ones > 0:
            return n - ones

        best = float('inf')

        for i in range(n):
            g = nums[i]
            for j in range(i + 1, n):
                g = gcd(g, nums[j])
                if g == 1:
                    best = min(best, j - i + 1)
                    break

        if best == float('inf'):
            return -1
        return (best - 1) + (n - 1)
