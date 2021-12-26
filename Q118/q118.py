
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]
        for i in range(1,numRows):
            prev_row = output[-1]
            new_row = []
            for i in range(len(prev_row)-1):
                new_row += [prev_row[i] + prev_row[i+1]]
            output += [[1]+ new_row+[1]]
        return output