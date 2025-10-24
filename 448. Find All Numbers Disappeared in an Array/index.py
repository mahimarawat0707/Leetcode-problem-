from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return list(set(range(1, n + 1)) - set(nums))


if __name__ == "__main__":
    nums = [4, 3, 2, 7, 8, 2, 3, 1]

    solution = Solution()
    missing = solution.findDisappearedNumbers(nums)

    print("Missing numbers:", missing)
