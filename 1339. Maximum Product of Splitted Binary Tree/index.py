from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7

        # Step 1: DFS to convert each node's value into subtree sum
        def dfs(node):
            if not node:
                return 0

            node.val += dfs(node.left) + dfs(node.right)
            return node.val

        total = dfs(root)  # Total sum of entire tree

        ans = 0
        q = deque([root])

        # Step 2: BFS to find best product
        while q:
            node = q.popleft()
            if not node:
                continue

            current_product = (total - node.val) * node.val
            ans = max(ans, current_product)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return ans % MOD
