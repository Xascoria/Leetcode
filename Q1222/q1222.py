from tkinter.messagebox import QUESTION
from typing import List

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        output = []

        for cx in range(-1, 2):
            for cy in range(-1, 2):
                if cx == cy == 0:
                    continue

                cur_x = king[0] + cx
                cur_y = king[1] + cy
                while 0 <= cur_x < 8 and 0 <= cur_y < 8:
                    if [cur_x, cur_y] in queens:
                        output += [[cur_x, cur_y]]
                        break
                    cur_x += cx
                    cur_y += cy
        return output