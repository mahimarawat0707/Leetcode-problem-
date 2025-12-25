class Solution:
    def sumScores(self, s: str) -> int:
        n = len(s)
        dp = [1] * n
        lps = [0] * n
        j = 0
        for i in range(1, n):
            while j and s[i] != s[j]:
                j = lps[j - 1]
            
            if s[i] == s[j]:
                dp[i] += dp[j]
                j = lps[i] = j + 1
                
        return sum(dp)