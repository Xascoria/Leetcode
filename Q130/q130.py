from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        trans = ((-1,0),(1,0),(0,-1),(0,1))
        flood_set = set()
        for i in range(len(board[0])):
            if board[0][i] == "O":
                flood_set.add((0,i))
            if board[-1][i] == "O":
                flood_set.add((len(board)-1,i))
        for i in range(1,len(board)-1):
            if board[i][0] == "O":
                flood_set.add((i,0))
            if board[i][-1] == "O":
                flood_set.add((i, len(board[0])-1 ))
        
        while flood_set:
            x,y = flood_set.pop()
            for i,j in trans:
                if 0<=x+i<len(board) and 0<=y+j<len(board[0]) and board[x+i][y+j] == "O":
                    flood_set.add( (x+i,y+j) )
            board[x][y] = "U"

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "U":
                    board[i][j] = "O"