from typing import List
from math import inf

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: (p[0], -p[1]))

        ans = 0

        for i, (_, y1) in enumerate(points):
            maxY = -inf
            for _, y2 in points[i + 1:]:
                if maxY < y2 <= y1:
                    ans += 1
                    maxY = y2

        return ans

if __name__ == "__main__":
    sol = Solution()
    test_points = [[1,3],[2,2],[3,1]]
    print("Number of valid pairs:", sol.numberOfPairs(test_points))
