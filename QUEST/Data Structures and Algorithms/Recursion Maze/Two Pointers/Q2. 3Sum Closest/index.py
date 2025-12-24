from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort the array first
        nums.sort()
        
        # Initialize result with the sum of first three elements
        result = nums[0] + nums[1] + nums[2]

        # Iterate through the array
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            # Two-pointer approach
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                # Update result if this total is closer to target
                if abs(target - total) < abs(target - result):
                    result = total

                # Move pointers based on comparison with target
                if total == target:
                    return target
                elif total < target:
                    left += 1
                else:
                    right -= 1

        return result


# Example usage
if __name__ == "__main__":
    sol = Solution()
    nums = [-1, 2, 1, -4]
    target = 1
    print(sol.threeSumClosest(nums, target))  # Output: 2
