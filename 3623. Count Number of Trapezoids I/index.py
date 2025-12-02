from typing import List
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        # Count how many points lie on each horizontal line (same y)
        cnt = {}
        for x, y in points:
            cnt[y] = cnt.get(y, 0) + 1
        
        # For each line y, number of ways to choose 2 points = c = C(cnt[y], 2)
        # A trapezoid needs two horizontal sides: choose two different horizontal lines,
        # and choose 2 points on each line. So sum over pairs of lines: c1 * c2.
        # We can compute this efficiently by accumulating.
        total_pairs = 0     # sum of c for lines we've processed so far
        answer = 0
        for y, num in cnt.items():
            if num >= 2:
                c = num * (num - 1) // 2
                # All previously counted pairs of horizontal sides (from previous lines)
                # can pair with c (current line) to form trapezoids.
                answer = (answer + total_pairs * c) % MOD
                total_pairs = (total_pairs + c) % MOD
        
        return answer
