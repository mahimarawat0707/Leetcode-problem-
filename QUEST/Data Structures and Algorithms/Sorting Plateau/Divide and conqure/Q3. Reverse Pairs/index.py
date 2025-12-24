class Solution:
    def reversePairs(self, nums):
        return self.merge_sort(nums, 0, len(nums) - 1)

    def merge_sort(self, nums, start, end):
        if start >= end:
            return 0

        mid = (start + end) // 2
        count = self.merge_sort(nums, start, mid)
        count += self.merge_sort(nums, mid + 1, end)
        count += self.count_pairs(nums, start, mid, end)
        self.merge(nums, start, mid, end)
        return count

    def count_pairs(self, nums, start, mid, end):
        count = 0
        j = mid + 1
        for i in range(start, mid + 1):
            while j <= end and nums[i] > 2 * nums[j]:
                j += 1
            count += j - (mid + 1)
        return count

    def merge(self, nums, start, mid, end):
        temp = []
        left, right = start, mid + 1

        while left <= mid and right <= end:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1

        while left <= mid:
            temp.append(nums[left])
            left += 1
        while right <= end:
            temp.append(nums[right])
            right += 1

        for i in range(len(temp)):
            nums[start + i] = temp[i]
            