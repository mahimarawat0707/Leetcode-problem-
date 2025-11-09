class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 2:
            return s

        start, max_len = 0, 0

        def expand(left: int, right: int) -> None:
            nonlocal start, max_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_len = right - left + 1
                if current_len > max_len:
                    max_len = current_len
                    start = left
                left -= 1
                right += 1

        for i in range(len(s)):
            expand(i, i)        # Odd length palindromes
            expand(i, i + 1)    # Even length palindromes

        return s[start:start + max_len]
