class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        tree1 = [None]
        tree2 = [None]
        def recursion(cur_node, tree, arr_index):
            if cur_node == None:
                return

            if arr_index >= len(tree):
                tree.extend( None for _ in range(arr_index-len(tree)+1) )
            tree[arr_index] = cur_node.val

            recursion(cur_node.left, tree, 2*arr_index+1)
            recursion(cur_node.right, tree, 2*arr_index+2)

        recursion(p, tree1, 0)
        recursion(q, tree2, 0)

        return tree1 == tree2