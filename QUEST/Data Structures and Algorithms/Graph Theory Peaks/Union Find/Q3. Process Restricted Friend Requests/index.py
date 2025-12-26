from typing import List


class DSU:
    def __init__(self, n: int):
        self.n = n
        self.p = list(range(n + 1))
        self.size = [1] * (n + 1)
        self.restrictions = [set() for _ in range(n + 1)]

    def find(self, u: int) -> int:
        if self.p[u] != u:
            self.p[u] = self.find(self.p[u])
        return self.p[u]

    def add_restriction(self, a: int, b: int) -> None:
        pa, pb = self.find(a), self.find(b)
        if pa != pb:
            self.restrictions[pa].add(pb)
            self.restrictions[pb].add(pa)

    def can_unite(self, a: int, b: int) -> bool:
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return True
        return pb not in self.restrictions[pa]

    def unite(self, a: int, b: int) -> bool:
        if not self.can_unite(a, b):
            return False

        pa, pb = self.find(a), self.find(b)
        if pa != pb:
            # Union by size (small into big = faster)
            if self.size[pa] < self.size[pb]:
                pa, pb = pb, pa

            # Merge restriction sets
            self.restrictions[pa].update(self.restrictions[pb])
            for other in self.restrictions[pb]:
                self.restrictions[other].remove(pb)
                self.restrictions[other].add(pa)

            self.size[pa] += self.size[pb]
            self.p[pb] = pa

        return True


class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        dsu = DSU(n)

        for u, v in restrictions:
            dsu.add_restriction(u, v)

        return [dsu.unite(u, v) for u, v in requests]
