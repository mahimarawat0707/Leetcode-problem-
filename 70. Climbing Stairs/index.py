class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        first, second = 1, 2

        for i in range(3, n + 1):
            third = first + second
            first, second = second, third

        return second
