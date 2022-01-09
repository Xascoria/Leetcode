from typing import List


from itertools import islice
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.row_caching = {}
        for row in range(len(matrix)):
            pass

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        output = 0
        for i in range(row1, row2+1):
            if (i, col1, col2) in self.row_caching:
                output += self.row_caching[(i, col1, col2)]
                continue
            if col2 + 1 - col1 > len(self.matrix[0])//2:
                ans = sum(self.matrix[i][col1:col2+1])
            else:
                ans = self.row_sums [i] - sum(self.matrix[i][:col1]) - sum(self.matrix[i][col2+1:])
            self.row_caching[(i, col1, col2)] = ans
            output += ans
        return output



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)