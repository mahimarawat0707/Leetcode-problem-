from typing import List
from bisect import bisect_left
from collections import defaultdict

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        rows = defaultdict(list)
        cols = defaultdict(list)

        # Build row and column maps
        for x, y in buildings:
            rows[x].append(y)
            cols[y].append(x)

        # Sort the lists for binary search
        for k in rows:
            rows[k].sort()
        for k in cols:
            cols[k].sort()

        covered = 0

        # Check each building
        for x, y in buildings:
            ry = rows[x]      # all y's in this row
            cx = cols[y]      # all x's in this column

            pos_y = bisect_left(ry, y)
            pos_x = bisect_left(cx, x)

            has_left = pos_y > 0
            has_right = pos_y < len(ry) - 1
            has_above = pos_x > 0
            has_below = pos_x < len(cx) - 1

            if has_left and has_right and has_above and has_below:
                covered += 1

        return covered


if __name__ == "__main__":
    sol = Solution()
    print(sol.countCoveredBuildings(3, [[1,2],[2,2],[3,2],[2,1],[2,3]]))  # 1
    print(sol.countCoveredBuildings(3, [[1,1],[1,2],[2,1],[2,2]]))        # 0
    print(sol.countCoveredBuildings(5, [[1,3],[3,2],[3,3],[3,5],[5,3]]))  # 1
