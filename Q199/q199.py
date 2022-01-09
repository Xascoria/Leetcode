# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None: return []
        output_arr = []
        def recursion(cur_node:TreeNode, cur_layer):
            if cur_layer > len(output_arr):
                output_arr.append(cur_node.val)

            if cur_node.right != None:
                recursion(cur_node.right, cur_layer+1)
            if cur_node.left != None:
                recursion(cur_node.left, cur_layer+1)
        recursion(root, 1)
        return output_arr