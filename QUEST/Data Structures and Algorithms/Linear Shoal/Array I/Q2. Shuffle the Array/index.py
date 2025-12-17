from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])
        return result

if __name__ == "__main__":
    nums = [2, 5, 1, 3, 4, 7]
    n = 3

    sol = Solution()
    output = sol.shuffle(nums, n)

    print("Input :", nums)
    print("Output:", output)
