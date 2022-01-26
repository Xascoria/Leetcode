from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left_tree = []
        right_tree = []

        def recursion(root, cur_index):
            nonlocal left_tree
            if cur_index >= len(left_tree):
                left_tree += [None] * (cur_index - len(left_tree)+1)

            left_tree[cur_index] = root.val
            if root.left != None:
                recursion(root.left, 2*cur_index+1)
            if root.right != None:
                recursion(root.right, 2*cur_index+2)
        def recursion_right(root, cur_index):
            nonlocal right_tree
            if cur_index >= len(right_tree):
                right_tree += [None] * (cur_index - len(right_tree)+1)

            right_tree[cur_index] = root.val
            if root.right != None:
                recursion_right(root.right, 2*cur_index+1)
            if root.left != None:
                recursion_right(root.left, 2*cur_index+2)

        if root.left != None: recursion(root.left, 0)
        if root.right != None: recursion_right(root.right, 0)

        print(left_tree)
        print(right_tree)
        return left_tree == right_tree