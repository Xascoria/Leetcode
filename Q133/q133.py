
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None: return None

        arr = [None] * 101
        output = [None] * 101

        to_be_processed = [node]
        while to_be_processed:
            node = to_be_processed.pop(0)
            output[node.val] = Node(node.val)
            arr[node.val] = node
            for neigh in node.neighbors:
                if arr[neigh.val] == None:
                    to_be_processed.append( neigh )
        
        for ind,outnode in enumerate(output):
            if outnode != None:
                for neigh in arr[ind].neighbors:
                    outnode.neighbors.append( output[neigh.val] )

        return output[1]