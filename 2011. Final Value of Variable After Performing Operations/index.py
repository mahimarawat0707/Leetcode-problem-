from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for op in operations:
            if "++" in op:
                x += 1
            else:
                x -= 1
        return x

if __name__ == "__main__":
    operations = ["--X", "X++", "X++"]
    sol = Solution()
    print("Final value of X:", sol.finalValueAfterOperations(operations))
