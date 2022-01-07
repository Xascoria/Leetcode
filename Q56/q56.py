from functools import cache
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged_intervals = [None] * 10001
        for i,j in intervals:
            cur_start = i
            cur_end = j
            for k in range(i,j+1):
                if merged_intervals[k] != None:
                    cur_start = min(cur_start, merged_intervals[k][0])
                    cur_end   = max(cur_end, merged_intervals[k][1])
            
            for k in range(cur_start, cur_end+1):
                merged_intervals[k] = (cur_start, cur_end)

            print(merged_intervals[:10])
        a = set(merged_intervals)
        a.remove(None)
        return a

x = Solution()
print( x.merge([[2,3],[4,6],[5,7],[3,4]]) )