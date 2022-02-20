from typing import List

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        x_count = o_count = 0
        for i in board:
            x_count += i.count('X')
            o_count += i.count('O')
        if not (x_count >= o_count and (x_count - o_count) <= 1):
            return False
        
        win_conds = board + [i+j+k for i,j,k in zip(*board)] + [board[0][0] + board[1][1] + board[2][2], board[0][2] + board[1][1] + board[2][0]]
        x_win = "XXX" in win_conds
        o_win = "OOO" in win_conds
        if x_win and o_win:
            return False
        if x_win and (x_count <= o_count):
            return False
        if o_win and (x_count != o_count):
            return False

        return True

x = Solution()
print( x.validTicTacToe(["XXA", '   ','O O']) )