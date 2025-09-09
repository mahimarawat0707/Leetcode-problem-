class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)  
        dp[1] = 1  

        for day in range(1, n + 1):
            for share_day in range(day + delay, min(n + 1, day + forget)):
                dp[share_day] = (dp[share_day] + dp[day]) % MOD

        return sum(dp[n - forget + 1: n + 1]) % MOD
