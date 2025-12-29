from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:

        # Recursive function to construct tree
        def construct_tree(cur_node_val: int) -> TreeNode:
            new_node = TreeNode(cur_node_val)

            if cur_node_val in children_hashmap:
                left_child, right_child = children_hashmap[cur_node_val]

                if left_child is not None:
                    new_node.left = construct_tree(left_child)

                if right_child is not None:
                    new_node.right = construct_tree(right_child)

            return new_node

        children_set = set()
        children_hashmap = {}

        # Build parent → [left, right] map
        for parent, child, isleft in descriptions:
            if parent not in children_hashmap:
                children_hashmap[parent] = [None, None]

            children_set.add(child)
            index = 0 if isleft else 1
            children_hashmap[parent][index] = child

        # Find root (parent that is never a child)
        head_node_val = None
        for parent in children_hashmap:
            if parent not in children_set:
                head_node_val = parent
                break

        return construct_tree(head_node_val)
