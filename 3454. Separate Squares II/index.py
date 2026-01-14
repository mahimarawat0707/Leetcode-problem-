from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []

        # Create sweep-line events
        for x, y, l in squares:
            events.append((y, 1, x, x + l))      # square starts
            events.append((y + l, -1, x, x + l)) # square ends

        events.sort()

        xs = []
        prev_y = events[0][0]
        total_area = 0
        areas = []

        def union_len(intervals):
            """Returns the total union length of x-intervals."""
            intervals.sort()
            res = 0
            end = -10**30

            for a, b in intervals:
                if a > end:
                    res += b - a
                    end = b
                elif b > end:
                    res += b - end
                    end = b

            return res

        # Sweep line over y-axis
        for y, typ, x1, x2 in events:
            if y > prev_y and xs:
                height = y - prev_y
                width = union_len(xs)
                areas.append((prev_y, height, width))
                total_area += height * width

            if typ == 1:
                xs.append((x1, x2))
            else:
                xs.remove((x1, x2))

            prev_y = y

        # Find y where half the area is accumulated
        half = total_area / 2
        acc = 0

        for y, h, w in areas:
            block_area = h * w
            if acc + block_area >= half:
                return y + (half - acc) / w
            acc += block_area

        return 0.0
