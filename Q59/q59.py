from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def recursion(cur_start,cur_height):
            if cur_height == 1:
                return [[cur_start]]

            if cur_height == 2:
                return [[cur_start, cur_start+1], [cur_start+3, cur_start+2]]

            first_row = [*range(cur_start, cur_start+cur_height)]
            next_start = cur_start+cur_height
            side_row = [*range(next_start, next_start+cur_height-2)]
            next_start = next_start+cur_height-2
            bottom_row = [*range(next_start+cur_height-1, next_start-1, -1)]
            next_start = next_start+cur_height
            left_row = [*range(next_start+cur_height-3, next_start-1, -1)]

            res = recursion(left_row[0]+1, cur_height-2)
            middle = [sum(a,[]) for a in zip([[i]for i in left_row], res, [[i]for i in side_row])]

            return [first_row] + middle + [bottom_row]

        return recursion(1, n)

x = Solution()
print( x.generateMatrix(5) )
#y = [*zip([[16],[15],[14]],[[17, 18, 19], [24, 25, 20], [23, 22, 21]],[[6],[7],[8]])]
#middle = [sum(a,[]) for a in y]
# Current ans: [(16, [17, 18, 19], 6), (15, (24, 25, 20), 7), (14, [23, 22, 21], 8)]
# Wanted output: [[16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 19, 20, 21, 8]]
#print(y)
#print(middle)