class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        output = 0
        trans = ((0,1),(0,-1),(1,0),(-1,0))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    output += 1
                    stack = set([(i,j)])
                    while stack:
                        k,l = stack.pop()
                        for cx, cy in trans:
                            if 0<=k+cx<len(board) and 0<=l+cy<len(board[0]) and board[k+cx][l+cy] == "X":
                                stack.add((k+cx,l+cy ))
                        board[k][l] = "U"
        return output