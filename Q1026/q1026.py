from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def recursion_tranverser(current_node, max_ans, min_ans):
            new_max = max(max_ans, current_node.val)
            new_min = min(min_ans, current_node.val)
            output = []
            if current_node.left != None:
                output += [recursion_tranverser(current_node.left, new_max, new_min)]
            if current_node.right != None:
                output += [recursion_tranverser(current_node.right, new_max, new_min)]
            output += [max(abs(max_ans-current_node.val), abs(min_ans-current_node.val))]
            return max(output)
        return recursion_tranverser(root, root.val, root.val)

