from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)

        # Small input? Just sort and pair
        if n <= 200:
            nums.sort()
            res = 0
            for i in range(n // 2):
                res = max(res, nums[i] + nums[n - 1 - i])
            return res

        # Find max value in nums
        maxi = 0
        for v in nums:
            if v > maxi:
                maxi = v

        # Frequency array
        freq = [0] * (maxi + 1)
        for v in nums:
            freq[v] += 1

        # Two pointers
        i, j = 0, maxi
        while i <= maxi and freq[i] == 0:
            i += 1
        while j >= 0 and freq[j] == 0:
            j -= 1

        res = 0
        pairs = n // 2

        while pairs > 0:
            res = max(res, i + j)
            freq[i] -= 1
            freq[j] -= 1

            if freq[i] == 0:
                while i <= maxi and freq[i] == 0:
                    i += 1

            if freq[j] == 0:
                while j >= 0 and freq[j] == 0:
                    j -= 1

            pairs -= 1

        return res
