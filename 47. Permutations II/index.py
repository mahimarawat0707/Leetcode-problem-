from typing import List
from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        counter = Counter(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for num in list(counter.keys()):
                if counter[num] > 0:
                    path.append(num)
                    counter[num] -= 1
                    backtrack(path)
                    counter[num] += 1
                    path.pop()

        backtrack([])
        return res
