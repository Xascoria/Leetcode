from graphlib import CycleError
import re
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None: return []
        def recursion(cur_node: TreeNode):
            output = []

            if cur_node.left != None:
                output += recursion(cur_node.left)
            
            if cur_node.right != None:
                output += recursion(cur_node.right)

            output += [cur_node.val]

            return output

        return recursion(root)