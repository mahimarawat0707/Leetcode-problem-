from typing import List

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)

        # prefix sums to get power in O(1)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stations[i]

        def can(min_power):
            extra = k
            add = [0] * (n + 1)  # difference array
            added = 0  # running sum from difference array

            for i in range(n):
                added += add[i]

                # power supplied currently to city i
                left = max(0, i - r)
                right = min(n - 1, i + r)
                current_power = (prefix[right + 1] - prefix[left]) + added

                if current_power < min_power:
                    need = min_power - current_power
                    if need > extra:
                        return False

                    extra -= need
                    added += need

                    # remove this addition when it stops affecting windows
                    remove_index = min(n, i + r + r + 1)
                    add[remove_index] -= need

            return True

        low, high = 0, sum(stations) + k  # maximum achievable minimum

        while low < high:
            mid = (low + high + 1) // 2
            if can(mid):
                low = mid
            else:
                high = mid - 1

        return low
