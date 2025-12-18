from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()  # sort stones initially
        
        while stones:
            s1 = stones.pop()  # the heaviest stone
            if not stones:  # if this is the last stone
                return s1
            
            s2 = stones.pop()  # the second-heaviest stone
            if s1 > s2:
                # remaining stone after smashing
                remaining = s1 - s2
                # find the correct index to keep list sorted
                for i in range(len(stones)+1):
                    if i == len(stones) or stones[i] >= remaining:
                        stones.insert(i, remaining)
                        break
            # if s1 == s2, both stones are destroyed and nothing is added
        
        return 0  # no stones left
