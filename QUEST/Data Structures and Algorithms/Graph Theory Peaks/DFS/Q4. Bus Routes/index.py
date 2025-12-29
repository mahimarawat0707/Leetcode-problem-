from typing import List
from collections import defaultdict, deque


class Solution:
    def numBusesToDestination(
        self,
        routes: List[List[int]],
        source: int,
        target: int
    ) -> int:

        if source == target:
            return 0

        # Map each stop to the buses that pass through it
        stop_to_buses = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].add(i)

        visited_buses = set()
        queue = deque([source])
        buses_taken = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                curr_stop = queue.popleft()
                if curr_stop == target:
                    return buses_taken

                for bus in stop_to_buses[curr_stop]:
                    if bus not in visited_buses:
                        visited_buses.add(bus)
                        queue.extend(routes[bus])

            buses_taken += 1

        return -1
