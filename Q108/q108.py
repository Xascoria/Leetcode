# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return None

        root_node = TreeNode(nums[len(nums)//2])
        def recursion(start_interval, end_interval, parent_node, is_left):
            if start_interval == end_interval:
                return

            cur_node = TreeNode(nums[(start_interval + end_interval)//2])
            if is_left:
                parent_node.left = cur_node
            else:
                parent_node.right = cur_node
            
            recursion( start_interval, (start_interval + end_interval)//2, cur_node, True )
            recursion( (start_interval + end_interval)//2 + 1, end_interval, cur_node, False )
        recursion( 0, len(nums)//2, root_node, True )
        recursion( len(nums)//2 + 1, len(nums), root_node, False )
        return root_node
            
            