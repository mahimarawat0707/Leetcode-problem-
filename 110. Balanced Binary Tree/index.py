class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.height(root) != -1

    def height(self, node: TreeNode) -> int:
        if not node:
            return 0  # Base case: empty tree has height 0

        # Recursively get the height of the left subtree
        leftHeight = self.height(node.left)
        if leftHeight == -1:
            return -1  # If the left subtree is unbalanced, return -1

        # Recursively get the height of the right subtree
        rightHeight = self.height(node.right)
        if rightHeight == -1:
            return -1  # If the right subtree is unbalanced, return -1

        # If the height difference between left and right subtrees is more than 1, return -1
        if abs(leftHeight - rightHeight) > 1:
            return -1

        # Return the height of the current node
        return max(leftHeight, rightHeight) + 1