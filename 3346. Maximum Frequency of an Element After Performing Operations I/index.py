from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        if not nums:
            return 0

        min_val = min(nums)
        max_val = max(nums)
        # We only need to consider targets T in range [min_val - k, max_val + k]
        # But values are >= 1 in constraints; allow index 0 as buffer
        MAX = max_val + k

        # frequency array of values from 0..MAX
        freq = [0] * (MAX + 1)
        for v in nums:
            freq[v] += 1

        # prefix sum for fast interval queries
        pref = [0] * (MAX + 1)
        running = 0
        for i in range(MAX + 1):
            running += freq[i]
            pref[i] = running

        def range_sum(l: int, r: int) -> int:
            if l > r:
                return 0
            if l <= 0:
                return pref[r]
            return pref[r] - pref[l - 1]

        ans = 0
        # Consider all possible integer targets T from 0..MAX
        for T in range(0, MAX + 1):
            l = max(0, T - k)
            r = min(MAX, T + k)
            can_make = range_sum(l, r)                 # all elements that can be turned into T
            already_T = freq[T] if 0 <= T <= MAX else 0
            # We can at most convert numOperations elements (distinct indices).
            # So final frequency for T is limited by can_make and already_T + numOperations
            cand = min(can_make, already_T + numOperations)
            if cand > ans:
                ans = cand

        return ans
