from collections import deque
from typing import List

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        dp = [0] * (n + 1)
        prefix = [0] * (n + 1)
        dp[0] = 1
        prefix[0] = 1

        left = 0
        minQ = deque()
        maxQ = deque()

        for right in range(n):
            x = nums[right]

            # maintain monotonic increasing deque for minimum
            while minQ and minQ[-1] > x:
                minQ.pop()
            minQ.append(x)

            # maintain monotonic decreasing deque for maximum
            while maxQ and maxQ[-1] < x:
                maxQ.pop()
            maxQ.append(x)

            # shrink window if invalid
            while maxQ[0] - minQ[0] > k:
                y = nums[left]
                if minQ[0] == y:
                    minQ.popleft()
                if maxQ[0] == y:
                    maxQ.popleft()
                left += 1

            # dp transition using prefix sum
            dp[right + 1] = (prefix[right] - (prefix[left - 1] if left > 0 else 0)) % MOD
            prefix[right + 1] = (prefix[right] + dp[right + 1]) % MOD

        return dp[n]


if __name__ == "__main__":
    sol = Solution()
    print(sol.countPartitions([1, 5, 6, 2], 3))  # test run
