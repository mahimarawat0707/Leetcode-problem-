class Solution:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num  # XOR cancels out duplicate numbers
        return result


if __name__ == "__main__":
    # Example input
    nums = [4, 1, 2, 1, 2]
    solution = Solution()
    single = solution.singleNumber(nums)
    print("The single number is:", single)
