from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        low = float('inf')
        high = float('-inf')
        total_area = 0

        # Calculate total area and vertical bounds
        for x, y, l in squares:
            total_area += l * l
            low = min(low, y)
            high = max(high, y + l)

        target_area = total_area / 2.0

        # Binary search for the correct y-level
        for _ in range(60):
            mid = (low + high) / 2.0
            curr_area = 0

            for _, y, l in squares:
                curr_y = max(0, min(l, mid - y))
                curr_area += l * curr_y

            if curr_area < target_area:
                low = mid
            else:
                high = mid

        return mid
