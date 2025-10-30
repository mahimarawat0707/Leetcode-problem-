from typing import List

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        if not target:
            return 0

        operations = target[0]
        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                operations += target[i] - target[i - 1]
        return operations
