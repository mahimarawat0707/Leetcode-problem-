class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def get_height_left(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        def get_height_right(node):
            height = 0
            while node:
                height += 1
                node = node.right
            return height

        left_height = get_height_left(root)
        right_height = get_height_right(root)

        if left_height == right_height:
           
            return (1 << left_height) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
