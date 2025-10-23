class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = list(map(int, s))
        n = len(digits)
        for size in range(n, 2, -1):
            for i in range(size - 1):
                digits[i] = (digits[i] + digits[i + 1]) % 10
        return digits[0] == digits[1]
