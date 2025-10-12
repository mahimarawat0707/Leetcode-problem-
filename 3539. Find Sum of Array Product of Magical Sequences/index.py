class Solution:
    def magicalSum(self, m: int, k: int, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        fact = [1] * (m + 1)
        invfact = [1] * (m + 1)
        for i in range(1, m + 1):
            fact[i] = (fact[i - 1] * i) % MOD

        invfact[m] = pow(fact[m], MOD - 2, MOD)
        for i in range(m - 1, -1, -1):
            invfact[i] = (invfact[i + 1] * (i + 1)) % MOD

        popcount_cache = {i: bin(i).count('1') for i in range(2 * m + 5)}

        dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(m + 1)]
        dp[0][0][0] = 1

        for val in nums:
            new_dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(m + 1)]

            terms = [0] * (m + 1)
            current_power = 1
            for c in range(m + 1):
                terms[c] = (current_power * invfact[c]) % MOD
                current_power = (current_power * val) % MOD

            for j in range(m + 1):
                for carry in range(m + 1):
                    for p in range(k + 1):
                        if dp[j][carry][p] == 0:
                            continue

                        for c in range(m - j + 1):
                            val_at_bit = c + carry
                            carry_new = val_at_bit // 2
                            p_new = p + (val_at_bit % 2)

                            if j + c <= m and carry_new <= m and p_new <= k:
                                contribution = (dp[j][carry][p] * terms[c]) % MOD
                                new_dp[j + c][carry_new][p_new] = (
                                    new_dp[j + c][carry_new][p_new] + contribution
                                ) % MOD
            dp = new_dp

        result_before_fact = 0
        for carry in range(2 * m + 5):
            final_carry_popcount = popcount_cache.get(carry, 0)
            for p in range(k + 1):
                if p + final_carry_popcount == k:
                    result_before_fact = (result_before_fact + dp[m][min(carry, m)][p]) % MOD

        final_answer = (result_before_fact * fact[m]) % MOD
        return final_answer
