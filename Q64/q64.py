from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        next_row = [grid[-1][-1]] * len(grid[0])
        for i in range(len(grid[0])-2,-1,-1):
            next_row[i] = grid[-1][i] + next_row[i+1]
        for i in range(len(grid)-2,-1,-1):
            cur_row = [0] * len(grid[0])
            cur_row[-1] = grid[i][-1] + next_row[-1]
            for j in range(len(grid[0])-2, -1, -1):
                cur_row[j] = grid[i][j] + min(cur_row[j+1], next_row[j])
            next_row = cur_row
        return next_row[0]

x = Solution()
print( x.minPathSum([[1,3,1],[1,5,1],[4,2,1]]) )