# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0
        current_depth = 0
        cur_nodes = [root]
        while len(cur_nodes) > 0:
            new_nodes = []
            for i in cur_nodes:
                if i.left != None:
                    new_nodes.append(i.left)
                if i.right != None:
                    new_nodes.append(i.right)
            cur_nodes = new_nodes
            current_depth += 1
        return current_depth
        