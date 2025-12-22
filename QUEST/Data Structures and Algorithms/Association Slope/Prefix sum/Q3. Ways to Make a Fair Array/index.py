class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        total_even =0
        total_odd = 0
        for i in range(len(nums)):
            if i%2 == 0:
                total_even +=nums[i]
            else:
                total_odd +=nums[i]

        prefix_sum_even = 0
        prefix_sum_odd = 0
        count = 0
        for i in range(len(nums)):
            if i%2 == 0:
                even_after_i = total_even - (prefix_sum_even+nums[i])
                even_before_i = prefix_sum_even
                odd_before_i = prefix_sum_odd
                odd_after_i = total_odd-prefix_sum_odd
                if odd_before_i+even_after_i == even_before_i+odd_after_i:
                    count+=1
                prefix_sum_even +=nums[i]
            else:
                
                odd_after_i = total_odd - (prefix_sum_odd+nums[i])
                odd_before_i = prefix_sum_odd
                even_before_i = prefix_sum_even
                even_after_i = total_even-prefix_sum_even
                if even_before_i+odd_after_i == odd_before_i+even_after_i:
                    count+=1
                prefix_sum_odd +=nums[i]

        return count


# 2, 1, 8, 5

# remove 1--->2,8,5-1
        