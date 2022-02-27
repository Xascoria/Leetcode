from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        layers = {}

        def recursion(cur_node, cur_layer, root_index):
            nonlocal layers

            if cur_layer not in layers:
                layers[cur_layer] = []
            layers[cur_layer].append(root_index)

            if cur_node.left != None:
                recursion(cur_node.left, cur_layer+1, root_index*2 + 1)

            if cur_node.right != None:
                recursion(cur_node.right, cur_layer+1, root_index*2 + 2)

        recursion(root, 0, 0)
        print(layers)
        return max( max(layers[i])-min(layers[i]) for i in layers )+1