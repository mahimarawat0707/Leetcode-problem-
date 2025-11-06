from typing import List
from collections import defaultdict
import heapq

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # ---------- DSU (Union-Find) setup ----------
        parent = list(range(c + 1))
        size = [1] * (c + 1)

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return
            if size[pa] < size[pb]:
                pa, pb = pb, pa
            parent[pb] = pa
            size[pa] += size[pb]

        # Build DSU components
        for u, v in connections:
            union(u, v)

        # ---------- Create min-heaps for components ----------
        comps = defaultdict(list)  # root → heap of online stations
        offline = set()            # to mark offline stations

        # Insert all stations as initially online
        for station in range(1, c + 1):
            heapq.heappush(comps[find(station)], station)

        # ---------- Process Queries ----------
        result = []

        for query_type, x in queries:

            if query_type == 2:
                # Mark offline
                offline.add(x)

            else:  # query_type == 1
                if x not in offline:
                    # Online -> resolves itself
                    result.append(x)
                    continue

                # Offline → find smallest available station in component
                root = find(x)
                heap = comps[root]

                # Clean heap top (lazy removal of offline stations)
                while heap and heap[0] in offline:
                    heapq.heappop(heap)

                if heap:
                    result.append(heap[0])
                else:
                    result.append(-1)

        return result
