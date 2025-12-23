from typing import List

# Time Complexity: O(n log n)
# Space Complexity: O(1)

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        arr.sort()

        res = []
        minDiff = float('inf')

        # Find minimum absolute difference
        for i in range(n - 1):
            minDiff = min(minDiff, arr[i + 1] - arr[i])

        # Collect all pairs with that minimum difference
        for i in range(n - 1):
            if arr[i + 1] - arr[i] == minDiff:
                res.append([arr[i], arr[i + 1]])

        return res
