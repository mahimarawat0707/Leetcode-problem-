from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, p: List[List[int]]) -> int:
        Ans = 0

        for i in range(1, len(p)):
            Ans += max(
                abs(p[i][0] - p[i - 1][0]),
                abs(p[i][1] - p[i - 1][1])
            )

        return Ans


# Example usage
if __name__ == "__main__":
    points = [[1, 1], [3, 4], [-1, 0]]
    sol = Solution()
    print(sol.minTimeToVisitAllPoints(points))
