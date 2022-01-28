class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cx = cy = 0
        for i in moves:
            if i in "UD":
                cx += [1,-1][i=="U"]
            else:
                cy += [1,-1][i=="L"]
        return cx == cy == 0