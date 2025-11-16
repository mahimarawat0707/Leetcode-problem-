class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        count = 0
        current = 0
        
        for ch in s:
            if ch == '1':
                current += 1
            else:
                count += current * (current + 1) // 2
                current = 0
                
        # Add the last segment if it ends with '1'
        count += current * (current + 1) // 2
        
        return count % MOD
