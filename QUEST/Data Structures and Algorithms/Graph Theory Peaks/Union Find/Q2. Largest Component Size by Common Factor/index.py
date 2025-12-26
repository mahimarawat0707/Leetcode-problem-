from typing import List
from collections import Counter


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        mx = max(nums)
        nums_set = set(nums)

        # Parent array for Union-Find
        parent = [i for i in range(mx + 1)]

        # Find with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # Union two nodes
        def union(a, b):
            rootA = find(a)
            rootB = find(b)
            if rootA != rootB:
                parent[rootA] = rootB

        # Union all numbers with their factors
        for factor in range(2, mx + 1):
            for multiple in range(factor, mx + 1, factor):
                if multiple in nums_set:
                    union(factor, multiple)

        # Count the size of each connected component
        component_sizes = Counter(find(num) for num in nums_set)

        return max(component_sizes.values())
