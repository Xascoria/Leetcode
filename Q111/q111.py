from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def recursion(cur_node):
            if None == cur_node.left == cur_node.right:
                return 1

            output = float("inf")
            if cur_node.left != None:
                output = min(recursion(cur_node.left)+1, output)

            if cur_node.right != None:
                output = min(recursion(cur_node.right)+1, output)
            return output
        if root == None:
            return 0
        return recursion(root)