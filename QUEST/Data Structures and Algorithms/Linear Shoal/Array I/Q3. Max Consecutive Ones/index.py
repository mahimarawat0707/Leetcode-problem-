from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        current_count = 0

        for num in nums:
            if num == 1:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0

        return max_count


if __name__ == "__main__":
    nums1 = [1, 1, 0, 1, 1, 1]
    print("Input:", nums1)
    print("Output:", Solution().findMaxConsecutiveOnes(nums1))

    nums2 = [1, 0, 1, 1, 0, 1]
    print("\nInput:", nums2)
    print("Output:", Solution().findMaxConsecutiveOnes(nums2))
