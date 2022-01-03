from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        trans = ((-1,0),(1,0),(0,1),(0,-1))
        def recursion(path_so_far):
            if len(path_so_far) == len(word):
                return True

            last_x = path_so_far[-1][0]
            last_y = path_so_far[-1][1]
            for xc, yc in trans:
                new_c = (last_x+xc, last_y+yc)
                if 0<=last_x+xc<len(board) and 0<=last_y+yc<len(board[0]) and board[new_c[0]][new_c[1]] == word[len(path_so_far)] and new_c not in path_so_far:
                    if recursion(path_so_far + [new_c]):
                        return True
            return False


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    ans = recursion([(i,j)])
                    if ans:
                        return True
        
        return False