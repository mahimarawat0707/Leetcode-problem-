def triangleNumber(nums: list[int]) -> int:
    nums.sort()
    n = len(nums)
    count = 0
    
    for k in range(n - 1, 1, -1):  # Fix the largest side
        i, j = 0, k - 1
        while i < j:
            if nums[i] + nums[j] > nums[k]:
                count += j - i
                j -= 1
            else:
                i += 1
    return count

# Example test cases
if __name__ == "__main__":
    nums1 = [2, 2, 3, 4]
    nums2 = [4, 2, 3, 4]
    
    print("Input:", nums1, "-> Output:", triangleNumber(nums1))  # Expected 3
    print("Input:", nums2, "-> Output:", triangleNumber(nums2))  # Expected 4
