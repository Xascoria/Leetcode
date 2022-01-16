from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None: return []
        output = []
        def recursion(cur_node, cur_layer):
            if cur_layer == len(output):
                output.append([])
            output[cur_layer].append(cur_node.val)
            
            if cur_node.left != None:
                recursion(cur_node.left, cur_layer+1)
            if cur_node.right != None:
                recursion(cur_node.right, cur_layer+1)
        recursion(root, 0)
        return output