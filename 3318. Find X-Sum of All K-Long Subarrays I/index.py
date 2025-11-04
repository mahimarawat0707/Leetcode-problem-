from typing import List
from collections import defaultdict
import heapq

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        freq = defaultdict(int)
        result = []

        # Build frequency for the first window
        for i in range(k):
            freq[nums[i]] += 1

        def calc_x_sum():
            # max heap: (-freq, -value)
            heap = [(-f, -v) for v, f in freq.items()]
            heapq.heapify(heap)

            total = 0
            count = 0

            while heap and count < x:
                f, v = heapq.heappop(heap)
                total += (-f) * (-v)
                count += 1

            return total

        result.append(calc_x_sum())

        # Slide the window
        for i in range(k, len(nums)):
            freq[nums[i]] += 1        # add new element
            freq[nums[i - k]] -= 1    # remove old element

            if freq[nums[i - k]] == 0:
                del freq[nums[i - k]]

            result.append(calc_x_sum())

        return result
