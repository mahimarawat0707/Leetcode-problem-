from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k

if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    solution = Solution()
    k = solution.removeDuplicates(nums)

    print(f"Number of unique elements: {k}")
    print(f"Array after removing duplicates: {nums[:k]}")
