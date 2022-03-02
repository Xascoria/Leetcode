from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        flatten = []
        negative_counts = 0

        for row in matrix:
            for i in row:
                if i <= 0:
                    negative_counts += 1
                flatten.append(abs(i))

        if negative_counts % 2 == 0:
            return sum(flatten)
        return sum(flatten) - min(flatten)*2

x = Solution()
print( x.maxMatrixSum([[10,-6,-6,-8],[-3,-7,-8,-9],[-4,-8,-5,-8],[-9,-9,-6,-8]]) )