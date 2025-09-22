from collections import Counter
from typing import List

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # Count the frequency of each element
        freq = Counter(nums)

        # Find the maximum frequency
        max_freq = max(freq.values())

        # Sum up all occurrences of elements that have the maximum frequency
        return sum(count for count in freq.values() if count == max_freq)


# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 2, 3, 1, 4]  # You can change the list to test
    result = solution.maxFrequencyElements(nums)
    print("Maximum frequency elements count:", result)
