class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        a = abs(x - z)
        b = abs(y - z)
        if a == b:
            return 0
        return 1 if a < b else 2
