import collections
import bisect

class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        if not power:
            return 0

        counts = collections.Counter(power)
        unique_powers = sorted(counts.keys())
        n = len(unique_powers)
        dp = [0] * n
        dp[0] = unique_powers[0] * counts[unique_powers[0]]

        for i in range(1, n):
            current_power = unique_powers[i]
            current_damage = current_power * counts[current_power]

            damage_if_skipped = dp[i-1]

            target = current_power - 2
            k_idx = bisect.bisect_left(unique_powers, target, hi=i)
            prev_idx = k_idx - 1
            prev_damage = dp[prev_idx] if prev_idx >= 0 else 0
            damage_if_taken = current_damage + prev_damage

            dp[i] = max(damage_if_skipped, damage_if_taken)

        return dp[-1]

if __name__ == "__main__":
    solver = Solution()

    power1 = [1, 1, 3, 4]
    output1 = solver.maximumTotalDamage(power1)
    print(f"Input: {power1}")
    print(f"Output: {output1} (Expected: 6)\n")

    power2 = [7, 1, 6, 6]
    output2 = solver.maximumTotalDamage(power2)
    print(f"Input: {power2}")
    print(f"Output: {output2} (Expected: 13)\n")
    
    power3 = [5, 9, 2, 10, 2, 7, 10, 9, 3, 8]
    output3 = solver.maximumTotalDamage(power3)
    print(f"Input: {power3}")
    print(f"Output: {output3} (Expected: 31)\n")