# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        output = ""
        def recursion(cur_node, cur_index):
            nonlocal output
            output += f"{cur_index}.{cur_node.val};"
            if cur_node.left != None:
                recursion(cur_node.left, cur_index*2 + 1)
            if cur_node.right != None:
                recursion(cur_node.right, cur_index*2+2)
        if root != None:
            recursion(root, 0)
        return output[:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        d = {}
        if len(data) == 0: return None
        for i in data.split(";"):
            a,b = map(int,i.split("."))
            d[a] = TreeNode(b)
        for ind in d:
            if ind*2+1 in d:
                d[ind].left = d[ind*2+1]
            if ind*2+2 in d:
                d[ind].right = d[ind*2+2]
        return d[0]

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))