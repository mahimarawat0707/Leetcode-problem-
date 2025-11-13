from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # Optimized math-based solution (O(n) time, O(1) extra space)
        n = len(nums)
        total_sum = sum(nums)
        unique_sum = sum(set(nums))
        
        duplicate = total_sum - unique_sum
        missing = (n * (n + 1)) // 2 - unique_sum
        
        return [duplicate, missing]

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    nums = [1, 2, 2, 4]
    print("Input:", nums)
    print("Output:", solution.findErrorNums(nums))  # Expected: [2, 3]

    # Example 2
    nums = [1, 1]
    print("\nInput:", nums)
    print("Output:", solution.findErrorNums(nums))  # Expected: [1, 2]
