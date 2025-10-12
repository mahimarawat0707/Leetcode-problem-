from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        
        if not nums:
            return res

        start = nums[0]

        for i in range(1, len(nums) + 1):
            if i == len(nums) or nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    res.append(str(start))
                else:
                    res.append(f"{start}->{nums[i - 1]}")
                
                if i < len(nums):
                    start = nums[i]
        
        return res


if __name__ == "__main__":
    nums = [0, 1, 2, 4, 5, 7]
    solution = Solution()
    print(solution.summaryRanges(nums))
