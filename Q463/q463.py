from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        trans = ((1,0),(0,1),(-1,0),(0,-1))
        output = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    for cx, cy in trans:
                        if 0<=i+cx<len(grid) and 0<=j+cy<len(grid[0]):
                            if grid[i+cx][j+cy] == 0:
                                output += 1
                        else:
                            output += 1
                #print(i,j,output)
        return output

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
x = Solution()
print( x.islandPerimeter(grid) )