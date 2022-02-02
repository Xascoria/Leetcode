# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def recursion(cur_node: TreeNode, is_on_left):
            if (cur_node.left == cur_node.right == None):
                if is_on_left:
                    return cur_node.val
                else:
                    return 0

            output = 0
            if cur_node.left != None:
                output += recursion(cur_node.left, True)
            if cur_node.right != None:
                output += recursion(cur_node.right, False)
            return output
        return recursion(root, False)