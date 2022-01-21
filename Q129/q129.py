from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def recursion(cur_node: TreeNode):
            if None == cur_node.left == cur_node.right:
                return [(cur_node.val, 1)]

            output = []
            if cur_node.left != None:
                for val, digit in recursion(cur_node.left):
                    output.append( ((val + cur_node.val * (10**digit)),digit+1) )

            if cur_node.right != None:
                for val, digit in recursion(cur_node.right):
                    output.append( ((val + cur_node.val * (10**digit)),digit+1) )

            return output
        #arr = recursion(root)
        #print(arr)
        return sum(i[0] for i in recursion(root))
