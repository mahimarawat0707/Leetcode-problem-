from collections import deque
from math import inf
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        idx = 0
        maxSum = -inf

        q = deque()
        q.append(root)
        level = 1

        while q:
            qz = len(q)
            curSum = 0

            for _ in range(qz):
                node = q.popleft()
                curSum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if curSum > maxSum:
                idx = level
                maxSum = curSum

            level += 1

        return idx
