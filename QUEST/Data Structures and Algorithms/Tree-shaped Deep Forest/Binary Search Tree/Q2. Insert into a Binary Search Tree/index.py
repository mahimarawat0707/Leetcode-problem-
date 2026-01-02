from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 🔁 Recursive approach
    # Time: O(h), Space: O(h)
    def insertIntoBST_recursive(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST_recursive(root.left, val)
        elif val > root.val:
            root.right = self.insertIntoBST_recursive(root.right, val)

        return root


    # 🔂 Iterative approach
    # Time: O(h), Space: O(1)
    def insertIntoBST_iterative(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        cur = root
        while True:
            if val < cur.val:
                if not cur.left:
                    cur.left = TreeNode(val)
                    return root
                cur = cur.left
            else:
                if not cur.right:
                    cur.right = TreeNode(val)
                    return root
                cur = cur.right
