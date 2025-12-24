from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        Reconstructs a binary tree from inorder and postorder traversal lists.
        """
        if not inorder or not postorder:
            return None

        # The last element of postorder is always the root
        root_val = postorder[-1]
        root = TreeNode(root_val)

        # Find the index of the root in inorder list
        index = inorder.index(root_val)

        # Recursively build left and right subtrees
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index + 1:], postorder[index:-1])

        return root


# Example usage:
if __name__ == "__main__":
    sol = Solution()
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    root = sol.buildTree(inorder, postorder)
    print(root.val)  # Output: 3
