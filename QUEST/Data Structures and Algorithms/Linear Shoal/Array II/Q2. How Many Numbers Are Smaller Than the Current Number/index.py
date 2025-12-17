from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Efficient O(n log n) approach using sorting
        sorted_nums = sorted(nums)
        rank_map = {}

        # Map each number to its first index (which represents how many numbers are smaller)
        for i, num in enumerate(sorted_nums):
            if num not in rank_map:
                rank_map[num] = i

        # Build result using the map
        result = [rank_map[num] for num in nums]
        return result


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [8, 1, 2, 2, 3]
    print("Input:", nums)
    print("Output:", solution.smallerNumbersThanCurrent(nums))  # Expected: [4, 0, 1, 1, 3]

    # Example 2
    nums = [6, 5, 4, 8]
    print("\nInput:", nums)
    print("Output:", solution.smallerNumbersThanCurrent(nums))  # Expected: [2, 1, 0, 3]

    # Example 3
    nums = [7, 7, 7, 7]
    print("\nInput:", nums)
    print("Output:", solution.smallerNumbersThanCurrent(nums))  # Expected: [0, 0, 0, 0]
