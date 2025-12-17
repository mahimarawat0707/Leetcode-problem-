from typing import List
from collections import deque


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()

        # Initialize the queue with indices
        for i in range(len(tickets)):
            queue.append(i)

        time = 0

        while queue:
            time += 1

            front = queue.popleft()
            tickets[front] -= 1

            # If person k finishes buying tickets
            if front == k and tickets[front] == 0:
                return time

            if tickets[front] > 0:
                queue.append(front)

        return time
