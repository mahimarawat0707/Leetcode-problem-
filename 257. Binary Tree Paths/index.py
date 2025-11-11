from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        def dfs(node, path):
            if not node:
                return

            path += str(node.val)

            if not node.left and not node.right:
                result.append(path)
                return

            dfs(node.left, path + "->")
            dfs(node.right, path + "->")

        dfs(root, "")
        return result


if __name__ == "__main__":

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)

    sol = Solution()
    print(sol.binaryTreePaths(root))   # Output: ['1->2->5', '1->3']
