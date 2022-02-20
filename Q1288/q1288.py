from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort( key=lambda x: (x[0], -x[1]) )
        
        output = 0
        cur_end = float('-inf')
        for i,j in intervals:
            if j > cur_end:
                output += 1
                cur_end = j
        return output

x = Solution()
print( x.removeCoveredIntervals([ [1,4],[1,3],[3,6],[2,8] ]) )