# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recursion(cur_node: TreeNode):
            if cur_node.left != None:
                res, min_left, max_left = recursion(cur_node.left)
                if not res:
                    return res, 0, 0
                if max_left >= cur_node.val:
                    return False, 0, 0 
            else:
                min_left = cur_node.val
            if cur_node.right != None:
                res, min_right, max_right = recursion(cur_node.right)
                if not res:
                    return res, 0, 0
                if min_right <= cur_node.val:
                    return False, 0, 0
            else:
                max_right = cur_node.val
            return True, min_left, max_right

        return recursion(root)[0]