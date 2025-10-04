from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        n = len(merged)
        
        if n % 2 == 1:
            return float(merged[n // 2])
        else:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2

nums1 = [1, 3]
nums2 = [2]

solution = Solution()
median = solution.findMedianSortedArrays(nums1, nums2)
print("Median:", median)

nums1 = [1, 2]
nums2 = [3, 4]
median = solution.findMedianSortedArrays(nums1, nums2)
print("Median:", median)
