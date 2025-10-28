from typing import List

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        valid_count = 0

        def simulate(arr, start, direction):
            nums = arr[:]  # copy
            curr = start
            while 0 <= curr < len(nums):
                if nums[curr] == 0:
                    curr += direction
                else:
                    nums[curr] -= 1
                    direction *= -1
                    curr += direction
            return all(x == 0 for x in nums)

        for i in range(n):
            if nums[i] == 0:
                # try left (-1)
                if simulate(nums, i, -1):
                    valid_count += 1
                # try right (+1)
                if simulate(nums, i, 1):
                    valid_count += 1

        return valid_count
