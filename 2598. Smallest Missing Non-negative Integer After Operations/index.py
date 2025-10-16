from collections import Counter
from typing import List

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        remainder_count = Counter(num % value for num in nums)
        
        i = 0
        while True:
            rem = i % value
            if remainder_count[rem] == 0:
                return i
            remainder_count[rem] -= 1
            i += 1
