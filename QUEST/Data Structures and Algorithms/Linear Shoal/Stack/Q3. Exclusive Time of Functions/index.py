from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            fid, typ, tims = log.split(':')
            fid, tims = int(fid), int(tims)

            if typ == "start":
                if stack:
                    res[stack[-1]] += tims - prev_time
                stack.append(fid)
                prev_time = tims
            else:
                res[stack.pop()] += tims - prev_time + 1
                prev_time = tims + 1

        return res
