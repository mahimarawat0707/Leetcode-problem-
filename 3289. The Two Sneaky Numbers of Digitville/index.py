from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        freq = {}
        result = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num, count in freq.items():
            if count >= 2:
                result.append(num)

        return result
