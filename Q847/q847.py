from typing import List

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        nodes_count = len(graph)
        termination_bit = 2**nodes_count - 1

        seens = set()
        queues = [(2**i, i, 0)for i in range(len(graph))]
        while True:
            bitmask, cur_node, path_length = queues.pop(0)

            
            if bitmask == termination_bit:
                return path_length 

            for i in range(len(graph[cur_node])):
                new = (bitmask | 2** graph[cur_node][i], graph[cur_node][i], path_length+1 )
                if (bitmask | 2** graph[cur_node][i], graph[cur_node][i]) not in seens:
                    seens.add( (bitmask | 2** graph[cur_node][i], graph[cur_node][i]) )
                    queues.append( new )

            
x = Solution()
print( x.shortestPathLength([[6,8],[2,9],[1,3,5],[2,6],[5],[2,6,4],[5,3,0,7],[6],[0],[1]]) )