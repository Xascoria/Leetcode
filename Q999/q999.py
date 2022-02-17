
from typing import List

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        x = y = 0
        for i,row in enumerate(board):
            if 'R' in row:
                x = i
                y = row.index('R')
                break
        output = 0
        for xc, yc in ((-1,0), (0,-1), (0,1), (1,0)):
            cur_x = x+xc
            cur_y = y+yc
            while 0<=cur_x<8 and 0<=cur_y<8:
                if board[cur_x][cur_y] in 'Bp':
                    output += board[cur_x][cur_y] == 'p'
                    break
                cur_x += xc
                cur_y += yc
        return output