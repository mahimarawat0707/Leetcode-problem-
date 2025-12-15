from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        total = 0
        des = 0
        prev = -1

        for x in prices:
            des = (-((x + 1) == prev) & des) + 1
            total += des
            prev = x

        return total
