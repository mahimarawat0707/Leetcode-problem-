class Solution:
    def maxOperations(self, s: str) -> int:
        ans = 0
        ones = 0
        n = len(s)
        
        for i, ch in enumerate(s):
            if ch == '1':
                ones += 1
            else:  # ch == '0'
                # if this '0' is followed by '1' or it's the last character,
                # it blocks all previous '1's from moving further → count them
                if i + 1 == n or s[i + 1] == '1':
                    ans += ones
        
        return ans
