from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lower_bound = 0
        upper_bound = len(matrix)
        middle = len(matrix)//2
        if matrix[middle][0] == target:
            return True
        while lower_bound+1 < upper_bound:
            if matrix[middle][0] > target:
                upper_bound = middle
            else:
                lower_bound = middle
            middle = (upper_bound+lower_bound)//2
            if matrix[middle][0] == target:
                return True

        line_index = middle
        lower_bound = 0
        upper_bound = len(matrix[0])
        middle = len(matrix[0])//2
        if matrix[line_index][middle] == target:
            return True
        while lower_bound+1 < upper_bound:
            if matrix[line_index][middle] > target:
                upper_bound = middle
            else:
                lower_bound = middle
            middle = (upper_bound+lower_bound)//2
            if matrix[line_index][middle] == target:
                return True

        return False

x = Solution()
print( x.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],11) )