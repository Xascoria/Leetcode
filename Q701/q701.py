from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(val)
            
        def recursion(cur_node):
            if val < cur_node.val:
                if cur_node.left == None:
                    cur_node.left = TreeNode(val)
                else:
                    recursion(cur_node.left)
            else:
                if cur_node.right == None:
                    cur_node.right = TreeNode(val)
                else:
                    recursion(cur_node.right)

        recursion(root)
        return root



            