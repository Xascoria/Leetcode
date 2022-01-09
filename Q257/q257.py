# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def recursion(cur_node: TreeNode):
            if cur_node.left == cur_node.right:
                return [str(cur_node.val)]
            
            out = []
            if cur_node.left != None:
                for i in recursion(cur_node.left):
                    out.append( str(cur_node.val)+"->"+i )
            if cur_node.right != None:
                for i in recursion(cur_node.right):
                    out.append( str(cur_node.val)+"->"+i )
            return out
        if root == None: return []
        return recursion(root)