from typing import List

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        # Step 1: Sort the input array
        nums.sort()
        
        # Step 2: Initialize a set to track used values
        used = set()
        
        # Step 3: Keep track of the last used value
        current = -float('inf')
        
        # Step 4: Iterate through each number
        for num in nums:
            # Calculate the smallest valid number greater than 'current'
            start = max(num - k, current + 1)
            
            # Check if we can assign this number within the allowed range
            if start <= num + k:
                used.add(start)
                current = start  # Update the last used value
        
        # Step 5: Return the total count of distinct numbers
        return len(used)
