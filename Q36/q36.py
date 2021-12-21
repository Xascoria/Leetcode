board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

from typing import List
def isValidSudoku(board: List[List[str]]) -> bool:
    nums = "123456789"
    for i in board:
        for j in nums:
            if i.count(j) > 1:
                return False

    for i in zip(*board):
        for j in nums:
            if i.count(j) > 1:
                return False

    for i in range(3):
        for j in range(3):
            arr = []
            for k in range(3):
                arr += board[i*3+k][j*3:j*3+3]
            for k in nums:
                if arr.count(k) > 1:
                    return False

    return True

print( isValidSudoku(board) )