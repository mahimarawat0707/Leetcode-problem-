from typing import List
from heapq import heappush, heappop, heapify


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Min-heap of available rooms
        ready = [r for r in range(n)]
        heapify(ready)

        # Min-heap of currently occupied rooms -> (end_time, room_number)
        rooms = []

        # Count of how many times each room is used
        res = [0] * n

        # Process meetings in sorted order
        for s, e in sorted(meetings):

            # Free rooms that have completed before current meeting starts
            while rooms and rooms[0][0] <= s:
                t, r = heappop(rooms)
                heappush(ready, r)

            # If a room is available, use it
            if ready:
                r = heappop(ready)
                heappush(rooms, (e, r))
            else:
                # Otherwise, delay the meeting until the earliest room is free
                t, r = heappop(rooms)
                new_end = t + (e - s)
                heappush(rooms, (new_end, r))

            res[r] += 1

        # Return the room with maximum usage
        return res.index(max(res))
