from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        bottom_row = [*map(int, matrix[-1])]
        area = max(bottom_row)

        for i in range(len(matrix)-2, -1, -1):
            cur_row = [0] * len(matrix[0])
            cur_row[-1] = matrix[i][-1] == "1"
            area = max(area, cur_row[-1])

            for j in range(len(matrix[0])-2, -1, -1):
                if matrix[i][j] == "1":
                    cur_row[j] = min(cur_row[j+1], bottom_row[j], bottom_row[j+1])+1
                    area = max(cur_row[j], area)
            bottom_row = cur_row

        return area*area

matrix = [["0","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","1"],["0","0","0","0","0"]]
x = Solution()
print(x.maximalSquare(matrix))