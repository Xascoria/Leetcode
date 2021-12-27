from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        cur_row = [1]
        for i in range(rowIndex):
            new_row = []
            for j in range(len(cur_row)-1):
                new_row += [cur_row[j] + cur_row[j+1]]
            cur_row = [1] + new_row + [1]
        return cur_row