import itertools
from typing import List

class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        m = len(mana)
        # Prefix sum of skill levels
        sps = list(itertools.accumulate(skill))
        current_start_time = 0

        for j in range(1, m):
            max_required_gap = 0
            for i in range(n):
                prev_sps = sps[i - 1] if i > 0 else 0
                current_gap = sps[i] * mana[j - 1] - prev_sps * mana[j]
                if current_gap > max_required_gap:
                    max_required_gap = current_gap
            current_start_time += max_required_gap

        total_time = current_start_time + sps[n - 1] * mana[m - 1]
        return total_time


def main():
    skill = [2, 3, 1]
    mana = [4, 2, 5]
    solution = Solution()
    result = solution.minTime(skill, mana)  # Fixed syntax here
    print("Minimum time:", result)


if __name__ == "__main__":
    main()
