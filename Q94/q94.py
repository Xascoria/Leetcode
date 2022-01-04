# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None: return None
        def recursion(current_node):
            output = []
            if current_node.left != None:
                output += recursion(current_node.left)
            output += [current_node.val]
            if current_node.right != None:
                output += recursion(current_node.right)
            return output
        return recursion(root)
    
    
        