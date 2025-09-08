from typing import List

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def contains_zero(x: int) -> bool:
            return '0' in str(x)
        
        for a in range(1, n):
            b = n - a
            if not contains_zero(a) and not contains_zero(b):
                return [a, b]
        
        return [-1, -1]
