from typing import List

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = 0
        
        # For each modulo class of index, store the minimum prefix sum seen so far
        min_prefix = [float('inf')] * k
        min_prefix[0] = 0   # prefix sum before starting
        
        best = -10**30  # sufficiently small
        
        for i, val in enumerate(nums):
            prefix += val
            r = (i + 1) % k  # bucket based on index + 1
            
            # Try forming a valid subarray ending here
            best = max(best, prefix - min_prefix[r])
            
            # Update the minimum prefix for this bucket
            min_prefix[r] = min(min_prefix[r], prefix)
        
        return best
