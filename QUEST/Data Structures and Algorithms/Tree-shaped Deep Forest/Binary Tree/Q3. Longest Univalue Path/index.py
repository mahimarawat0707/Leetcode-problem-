class Solution:
    def longestUnivaluePath(self, root):
        self.max = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left
            if node.right and node.right.val == node.val:
                right_arrow = right

            self.max = max(self.max, left_arrow + right_arrow + 1)
            return max(left_arrow, right_arrow) + 1

        dfs(root)
        return self.max - 1 if self.max > 0 else 0