from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        for i in range(1, n // 2 + 1):
            res.append(i)
            res.append(-i)
        if n % 2 == 1:
            res.append(0)
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.sumZero(4))
    print(sol.sumZero(5))
