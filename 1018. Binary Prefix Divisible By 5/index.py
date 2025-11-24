from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        curr = 0

        for bit in nums:
            curr = (curr * 2 + bit) % 5
            result.append(curr == 0)

        return result
