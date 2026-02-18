class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = n ^ (n >> 1)
        return (x & (x + 1)) == 0

if __name__ == "__main__":
    sol = Solution()
    print(sol.hasAlternatingBits(5))  # True (101 has alternating bits)
    print(sol.hasAlternatingBits(7))  # False (111 does not)
