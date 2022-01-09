from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        trans = ((1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1))
        for i in range(len(board)):
            for j in range(len(board[0])):
                neighbours_alive = 0
                for cx, cy in trans:
                    if 0<=i+cx<len(board) and 0<=j+cy<len(board[0]) and board[i+cx][j+cy] % 2 == 1:
                        neighbours_alive += 1
                if board[i][j] == 0:
                    if neighbours_alive == 3:
                        board[i][j] = 2
                else:
                    if neighbours_alive not in (2,3):
                        board[i][j] = 3

        # for i in board:
        #     print(i)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0

x = Solution()
print( x.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]) )