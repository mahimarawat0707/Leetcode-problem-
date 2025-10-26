from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        """
        Return a list of all self-dividing numbers between left and right (inclusive).
        A self-dividing number is divisible by every digit it contains and has no zeros.
        """
        def is_self_dividing(num: int) -> bool:
            original = num
            while num > 0:
                digit = num % 10
                # A self-dividing number cannot contain 0 or fail divisibility
                if digit == 0 or original % digit != 0:
                    return False
                num //= 10
            return True

        # Collect all self-dividing numbers in the range
        result = []
        for n in range(left, right + 1):
            if is_self_dividing(n):
                result.append(n)
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.selfDividingNumbers(1, 22))  
    # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
