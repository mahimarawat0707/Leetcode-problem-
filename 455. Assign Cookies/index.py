from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Sort both lists to use the smallest cookie for the least greedy child
        g.sort()
        s.sort()
        
        child = 0   # Index for children
        cookie = 0  # Index for cookies
        
        # Try to assign cookies to children
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                # If the cookie satisfies the child's greed
                child += 1
            # Move to the next cookie in either case
            cookie += 1
        
        return child
