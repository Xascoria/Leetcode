from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:return triangle[0][0]
        last_row = triangle[-1]
        value_arr = [ min(last_row[i], last_row[i+1]) for i in range(len(last_row)-1)]
        for i in range(len(triangle)-2,-1,-1):
            new_arr = [sum(i) for i in zip(triangle[i],value_arr)]
            value_arr = [ min(new_arr[i], new_arr[i+1]) for i in range(len(new_arr)-1)]
        return new_arr[0]

x = Solution()
print( x.minimumTotal([[2]]) )