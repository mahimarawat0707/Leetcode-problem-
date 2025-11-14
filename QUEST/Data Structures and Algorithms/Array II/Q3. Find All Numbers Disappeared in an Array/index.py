from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Mark numbers by flipping the sign at the corresponding index
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]

        # Collect positions that remain positive (those numbers never appeared)
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        return result

if __name__ == "__main__":
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    solution = Solution()
    missing_numbers = solution.findDisappearedNumbers(nums)
    print("Missing numbers:", missing_numbers)
