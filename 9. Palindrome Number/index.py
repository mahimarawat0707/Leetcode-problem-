class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_num = 0
        original = x

        while x > 0:
            reversed_num = reversed_num * 10 + (x % 10)
            x //= 10

        return original == reversed_num

if __name__ == "__main__":
    solution = Solution()
    test_cases = [121, -121, 10, 1221, 0]

    for num in test_cases:
        print(f"Is {num} a palindrome? → {solution.isPalindrome(num)}")
