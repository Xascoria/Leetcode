from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def recursion(current_node, upper_val):
            if current_node.left == current_node.right == None:
                if current_node.val + upper_val == targetSum:
                    return [[current_node.val]]
                return []
            
            output = []
            if current_node.left != None:
                res = recursion(current_node.left, upper_val + current_node.val)
                for i in res:
                    output.append([current_node.val] + i)
            if current_node.right != None:
                res = recursion(current_node.right, upper_val + current_node.val)
                for i in res:
                    output.append([current_node.val] + i)
            return output

        if root == None:
            return []
        return recursion(root, 0)

