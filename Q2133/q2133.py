from typing import List

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        compare_arr = [*range(1,len(matrix)+1)]
        for i in matrix:
            if sorted(i) != compare_arr:
                return False

        for i in zip(*matrix):
            if sorted(i) != compare_arr:
                return False

        return True