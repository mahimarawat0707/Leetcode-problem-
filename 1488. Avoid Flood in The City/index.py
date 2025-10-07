from bisect import bisect_right
from typing import List

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        res = [-1] * n
        full = set()
        lastRain = {}
        dryDays = []
        
        for i, lake in enumerate(rains):
            if lake == 0:
                dryDays.append(i)
                res[i] = 1
            else:
                if lake in full:
                    if lake not in lastRain:
                        return []
                    
                    idx = bisect_right(dryDays, lastRain[lake])
                    if idx == len(dryDays):
                        return []
                    
                    dry_day = dryDays.pop(idx)
                    res[dry_day] = lake
                    full.remove(lake)
                
                full.add(lake)
                lastRain[lake] = i
        
        return res
