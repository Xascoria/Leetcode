# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        left_tree = []
        right_tree = []
        using_left = True

        def recursion(cur_node):
            nonlocal left_tree
            nonlocal right_tree
            nonlocal using_left

            if cur_node.left != None:
                recursion(cur_node.left)
            if using_left:
                left_tree += [cur_node.val]
            else:
                right_tree += [cur_node.val]
            if cur_node.right != None:
                recursion(cur_node.right)

        if root1 != None: recursion(root1)
        using_left = False
        if root2 != None: recursion(root2)
        
        ptr1 = ptr2 = 0
        output = []
        while ptr1 != len(left_tree) and ptr2 != len(right_tree):
            if left_tree[ptr1] > right_tree[ptr2]:
                output.append( right_tree[ptr2] )
                ptr2 += 1
            else:
                output.append( left_tree[ptr1] )
                ptr1 += 1
        if ptr1 == len(left_tree):
            output += right_tree[ptr2:]
        else:
            output += left_tree[ptr1:]
        return output