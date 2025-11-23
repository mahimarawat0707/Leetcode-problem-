from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)

        rem1 = []
        rem2 = []

        for n in nums:
            if n % 3 == 1:
                rem1.append(n)
            elif n % 3 == 2:
                rem2.append(n)

        rem1.sort()
        rem2.sort()

        if total % 3 == 0:
            return total

        if total % 3 == 1:
            option1 = rem1[0] if rem1 else float('inf')
            option2 = rem2[0] + rem2[1] if len(rem2) >= 2 else float('inf')
            return total - min(option1, option2)

        option1 = rem2[0] if rem2 else float('inf')
        option2 = rem1[0] + rem1[1] if len(rem1) >= 2 else float('inf')
        return total - min(option1, option2)


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 6, 5, 1, 8]
    print(sol.maxSumDivThree(nums))  # Expected output: 18
