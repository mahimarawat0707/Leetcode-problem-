import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)

        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]

if __name__ == "__main__":
    k = 3
    nums = [4, 5, 8, 2]
    kthLargest = KthLargest(k, nums)

    print(kthLargest.add(3))   # returns 4
    print(kthLargest.add(5))   # returns 5
    print(kthLargest.add(10))  # returns 5
    print(kthLargest.add(9))   # returns 8
    print(kthLargest.add(4))   # returns 8
