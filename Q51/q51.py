from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        trans = [(1, -1), (1, 0), (1, 1)]
        board = [["b"]*n for _ in range(n)]
        def recursion(board, cur_index):
            if cur_index == n:
                return [["".join(i)for i in board]]

            output = []
            for i in range(n):
                if board[cur_index][i] == "b":
                    new_row = ["."]*n
                    new_row[i] = "Q"
                    new_board = board[:cur_index] + [new_row] + [row[:]for row in board[cur_index+1:]]
                    for xc, yc in trans:
                        start_x = cur_index
                        start_y = i
                        while 0 <= xc+start_x < n and 0 <= yc + start_y < n:
                            new_board[xc+start_x][yc + start_y] = "."
                            start_x += xc
                            start_y += yc
                    output += recursion(new_board, cur_index+1)
            return output

        return recursion(board, 0)

x = Solution()
print( x.solveNQueens(4) )