class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur = 0
        maxnum = 0
        
        for i in gain:
            cur += i
            maxnum = max(cur, maxnum)
        return maxnum