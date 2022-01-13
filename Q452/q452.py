from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:(x[0],x[1]))
        output = 1
        cur_ptr = 1
        cur_start = points[0][0]
        cur_end = points[0][1]
        while cur_ptr < len(points):
            if cur_start <= points[cur_ptr][0] <= cur_end or cur_start <= points[cur_ptr][1] <= cur_end:
                cur_start = max(cur_start, points[cur_ptr][0])
                cur_end = min(cur_end, points[cur_ptr][1])
            else:
                output += 1
                cur_start = points[cur_ptr][0]
                cur_end = points[cur_ptr][1]
            cur_ptr += 1

        return output 


x = Solution()
print( x.findMinArrowShots([[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]) )