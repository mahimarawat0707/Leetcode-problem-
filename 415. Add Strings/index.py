class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p1, p2 = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []

        while p1 >= 0 or p2 >= 0 or carry:
            x1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            x2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0

            total = x1 + x2 + carry
            carry = total // 10
            result.append(str(total % 10))

            p1 -= 1
            p2 -= 1

        return ''.join(reversed(result))


if __name__ == "__main__":
    sol = Solution()
    print(sol.addStrings("456", "77"))  # Output: 533
