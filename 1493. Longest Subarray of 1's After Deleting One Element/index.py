from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zeros = 0
        max_len = 0

        for right in range(len(nums)):
            # Count zeros in the current window
            if nums[right] == 0:
                zeros += 1

            # If more than one zero, shrink the window from the left
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            # Update the max length (subtract 1 because one zero is deleted)
            max_len = max(max_len, right - left)

        return max_len

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 0, 1]
    print(solution.longestSubarray(nums))  # Output: 3
