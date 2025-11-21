class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for ch in set(s):
            left = s.find(ch)
            right = s.rfind(ch)
            if right - left > 1:  # Must have space for a middle character
                mid_chars = set(s[left + 1:right])
                res += len(mid_chars)
        return res
