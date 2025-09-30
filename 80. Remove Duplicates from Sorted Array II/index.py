from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        # Pointer for the position to insert
        insert_pos = 2  

        for i in range(2, len(nums)):
            # Compare with element 2 steps behind
            if nums[i] != nums[insert_pos - 2]:
                nums[insert_pos] = nums[i]
                insert_pos += 1

        return insert_pos


# ---- Test the code ----
if __name__ == "__main__":
    nums = [0,0,1,1,1,1,2,3,3]
    sol = Solution()
    k = sol.removeDuplicates(nums)
    print("Length after removing duplicates:", k)
    print("Modified array:", nums[:k])