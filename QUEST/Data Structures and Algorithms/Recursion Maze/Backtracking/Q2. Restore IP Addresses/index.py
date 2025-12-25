from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(index: int, path: List[str]):
            # Base case: 4 parts formed
            if len(path) == 4:
                if index == len(s):
                    res.append(".".join(path))
                return

            # Try parts of length 1 to 3
            for length in range(1, 4):
                if index + length > len(s):
                    break

                part = s[index:index + length]

                # No leading zero allowed
                if part[0] == '0' and len(part) > 1:
                    continue

                # Value must be <= 255
                if int(part) > 255:
                    continue

                path.append(part)
                backtrack(index + length, path)
                path.pop()  # backtrack

        backtrack(0, [])
        return res
