from typing import List

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        # If total sum is odd → it's impossible for any partition to have even difference
        if total % 2 != 0:
            return 0
        
        # If total sum is even → **every** split between 0…i and i+1…end (for i from 0 to n-2) works.
        # There are n-1 such possible splits (since both subarrays must be non-empty).
        return len(nums) - 1
