class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1: return 0

        bottom_row = [1] * len(obstacleGrid[0])
        has_op = False
        for i in range(len(obstacleGrid[0])-2,-1,-1):
            if has_op:
                bottom_row[i] = 0
            elif obstacleGrid[-1][i] == 1:
                bottom_row[i] = 0
                has_op = True
            else:
                bottom_row[i] = bottom_row[i+1]
        for i in range(len(obstacleGrid)-2, -1, -1):
            cur_row = [(obstacleGrid[i][-1] != 1) and bottom_row[-1]] * len(obstacleGrid[0])
            for j in range(len(obstacleGrid[0])-2, -1, -1):
                if obstacleGrid[i][j] != 1:
                    cur_row[j] = bottom_row[j] + cur_row[j+1]
                else:
                    cur_row[j] = 0
            bottom_row = cur_row
        return int(bottom_row[0])
