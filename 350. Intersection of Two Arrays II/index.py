from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        result = []

        for num in count1:
            if num in count2:
                result.extend([num] * min(count1[num], count2[num]))
        
        return result

if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]

    print("Array 1:", nums1)
    print("Array 2:", nums2)
    print("Intersection:", solution.intersect(nums1, nums2))
