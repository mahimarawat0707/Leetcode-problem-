from collections import deque

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        seen = set()
        q = deque([s])
        res = s

        while q:
            curr = q.popleft()
            if curr in seen:
                continue
            seen.add(curr)

            # Update the smallest lexicographically
            res = min(res, curr)

            # Operation 1: Add 'a' to digits at odd indices
            arr = list(curr)
            for i in range(1, len(arr), 2):
                arr[i] = str((int(arr[i]) + a) % 10)
            added = "".join(arr)

            # Operation 2: Rotate the string to the right by b
            rotated = curr[-b:] + curr[:-b]

            # Push new states
            q.append(added)
            q.append(rotated)

        return res
