class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        neighbours = ((1,0),(0,1),(-1,0),(0,-1))
        turn = 0
        while True:
            to_be_rotten = set()
            has_fresh = False
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        for k, l in neighbours:
                            if 0<=i+k<len(grid) and 0<=j+l<len(grid[0]) and grid[i+k][j+l] == 2:
                                to_be_rotten.add((i,j))
                                break
                        else: has_fresh = True
            if len(to_be_rotten) == 0:
                return (turn,-1)[has_fresh]
            for i,j in to_be_rotten:
                grid[i][j] = 2
            turn += 1