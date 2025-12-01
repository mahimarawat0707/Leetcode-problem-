from typing import List

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        
        # Binary search range:
        # Minimum time = 0
        # Maximum possible time = total battery power divided by number of computers
        left, right = 0, sum(batteries) // n

        # Helper function to check if all computers can run for 't' time
        def can_run(t):
            total_power = 0
            for power in batteries:
                total_power += min(power, t)
            return total_power >= n * t

        # Binary search to find maximum feasible time
        while left < right:
            mid = (left + right + 1) // 2
            if can_run(mid):
                left = mid
            else:
                right = mid - 1

        return left
