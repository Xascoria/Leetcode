from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def recursion(cur_node):
            if cur_node.left == None and cur_node.right == None:
                return [cur_node.val]
            output = []
            if cur_node.left != None:
                for val in recursion(cur_node.left):
                    output += [val + cur_node.val]      
            if cur_node.right != None:
                for val in recursion(cur_node.right):
                    output += [val + cur_node.val]     
            return output
        if root == None: return False
        return targetSum in recursion(root)