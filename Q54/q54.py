from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def recursion(cur_mat):
            if len(cur_mat) == 1: 
                return cur_mat[0]

            if len(cur_mat) == 2:
                return cur_mat[0] + cur_mat[1][::-1]

            output = cur_mat[0][:]
            for i in range(1,len(cur_mat)-1):
                output += [cur_mat[i][-1]]
            output += cur_mat[-1][::-1]
            if len(cur_mat[0]) > 1:
                for i in range(len(cur_mat)-2,0,-1):
                    output += [cur_mat[i][0]]
            new_mat = [i[1:-1] for i in cur_mat[1:-1]]
            if len(new_mat[0]) > 0:
                return output + recursion(new_mat)
            return output
        return recursion(matrix)

x = Solution()
print( x.spiralOrder([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]) )
