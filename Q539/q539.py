from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        def get_time_val(string):
            a,b = string.split(':')
            return int(a)*60 + int(b)
        new_arr = [*map(get_time_val, timePoints)]
        return min(min(new_arr[i+1]-new_arr[i] for i in range(len(new_arr)-1)),1440 -new_arr[-1]+new_arr[0])