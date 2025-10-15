from typing import List

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        prev = 0
        cur = 1
        ans = 0
        
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                cur += 1
            else:
                ans = max(ans, cur // 2, min(prev, cur))
                prev = cur
                cur = 1
        
        ans = max(ans, cur // 2, min(prev, cur))
        
        return ans

if __name__ == "__main__":
    sol = Solution()
    
    print(sol.maxIncreasingSubarrays([2, 5, 7, 8, 9, 2, 3, 4, 3, 1]))
    print(sol.maxIncreasingSubarrays([1, 2, 3, 4, 4, 4, 4, 5, 6, 7]))
    print(sol.maxIncreasingSubarrays([1, 2, 3, 4]))
    print(sol.maxIncreasingSubarrays([5, 4, 3, 2, 1]))
