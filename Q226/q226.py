from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None: return root
        def recursion(cur_node):
            if cur_node.left != None:
                recursion(cur_node.left)

            if cur_node.right != None:
                recursion(cur_node.right)
            cur_node.left, cur_node.right = cur_node.right, cur_node.left
        recursion(root)
        return root