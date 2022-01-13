from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        def recursion(parent_val, cur_node):
            if None == cur_node.left == cur_node.right:
                return (parent_val << 1) + cur_node.val

            output = 0
            if cur_node.left != None:
                output += recursion((parent_val << 1) + cur_node.val, cur_node.left)
            if cur_node.right != None:
                output += recursion((parent_val << 1) + cur_node.val, cur_node.right)
            return output
        
        return recursion(0, root)