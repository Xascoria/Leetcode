from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        trans = ((1,0),(0,1),(-1,0),(0,-1))
        for row_index in range(len(matrix)):
            for col_index in range(len(matrix[0])):
                if matrix[row_index][col_index] == 0:
                    for i,j in trans:
                        cur_row = row_index+i
                        cur_col = col_index+j
                        while 0<=cur_row<len(matrix) and 0<=cur_col<len(matrix[0]) and (matrix[cur_row][cur_col] not in (0,"None")):
                            matrix[cur_row][cur_col] = None
                            cur_row += i
                            cur_col += j
        
        for row_index in range(len(matrix)):
            for col_index in range(len(matrix[0])):
                if matrix[row_index][col_index] == None:
                    matrix[row_index][col_index] = 0

x =  Solution()
print( x.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]) )
        