from math import factorial
from typing import List

class Solution:
    def countPermutations(self, a: List[int]) -> int:
        MOD = 10**9 + 7
        if len(a) == 0:
            return 0
        if a[0] < min(a[1:]):
            return factorial(len(a) - 1) % MOD
        else:
            return 0
