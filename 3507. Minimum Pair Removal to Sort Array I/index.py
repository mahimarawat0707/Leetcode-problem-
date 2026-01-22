from typing import List


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        
        def is_sorted(arr: List[int], n: int) -> bool:
            for i in range(1, n):
                if arr[i] < arr[i - 1]:
                    return False
            return True

        ans = 0
        n = len(nums)

        while not is_sorted(nums, n):
            ans += 1

            min_sum = float('inf')
            pos = -1

            for i in range(1, n):
                pair_sum = nums[i - 1] + nums[i]
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    pos = i

            nums[pos - 1] = min_sum

            for i in range(pos, n - 1):
                nums[i] = nums[i + 1]

            n -= 1

        return ans
