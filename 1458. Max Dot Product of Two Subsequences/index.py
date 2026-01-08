from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        memo = {}

        # dp(i, j) = max dot product of subsequences starting from index i and j
        def dp(i: int, j: int) -> int:
            
            # Base case: if either array is exhausted, no valid subsequence
            if i == len(nums1) or j == len(nums2):
                return float("-inf")

            # If already computed, return from memo
            if (i, j) in memo:
                return memo[(i, j)]

            take = nums1[i] * nums2[j]

            result = max(
                take + dp(i + 1, j + 1),  # take both and move forward
                take,                    # start a new subsequence here
                dp(i + 1, j),             # skip nums1[i]
                dp(i, j + 1)              # skip nums2[j]
            )

            memo[(i, j)] = result
            return result

        return dp(0, 0)
