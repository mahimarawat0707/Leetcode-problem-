from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):   # loop two times
            for num in nums:
                ans.append(num)
        return ans

if __name__ == "__main__":
    obj = Solution()
    nums = [1, 2, 1]
    print(obj.getConcatenation(nums))
