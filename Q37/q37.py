class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def get_neighbours(x,y):
            output = set()
            for i in range(9):
                if board[x][i] != ".":
                    output.add( board[x][i] )
                if board[i][y] != ".":
                    output.add( board[i][y] )

            for i in range(3):
                for j in range(3):
                    if board[x//3*3 + i][y//3*3 + j] != ".":
                        output.add( board[x//3*3 + i][y//3*3 + j] )

            return output
        
        def recursion():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        nb = get_neighbours(i,j)
                        possible_chars = {k for k in "123456789" if k not in nb}
                        #print(i,j, possible_chars)
                        if len(possible_chars) == 0:
                            return False
                        for k in possible_chars:
                            board[i][j] = k
                            if recursion():
                                return True
                        board[i][j] = "."
                        return False

            return True

        recursion()