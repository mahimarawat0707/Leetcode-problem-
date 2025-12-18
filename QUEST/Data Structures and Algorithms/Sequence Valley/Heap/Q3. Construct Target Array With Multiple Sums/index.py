from typing import List
from heapq import heapify, heappop, heappush

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        # Create a max-heap using negative values
        heap = [-num for num in target]
        total = sum(target)
        heapify(heap)
        
        while heap[0] != -1:  # Continue until the largest element is 1
            num = -heappop(heap)  # Get the largest element
            total -= num
            
            # If the largest number is too small or total is invalid
            if num <= total or total < 1:
                return False
            
            # Replace the largest element with its modulo of the rest
            num %= total
            total += num
            heappush(heap, -num or -total)  # Push back into heap
            
        return True
