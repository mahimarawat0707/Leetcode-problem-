from typing import List
from collections import Counter

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        left = Counter()
        right = Counter(nums)
        result = 0
        
        for x in nums:
            # remove current x from right, as we're treating it as middle now
            right[x] -= 1
            
            double_val = x * 2
            # count how many 2*x on left and right
            count_left = left.get(double_val, 0)
            count_right = right.get(double_val, 0)
            
            result = (result + count_left * count_right) % MOD
            
            # include current x into left for future iterations
            left[x] += 1
        
        return result
