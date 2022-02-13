from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        out = 0
        for i in range(len(mat)):
            a = i
            b = len(mat)-i-1
            if a == b:
                out += mat[i][a]
            else:
                out += mat[i][a] + mat[i][b]
        return out