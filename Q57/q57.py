from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        inserted = False
        output = []
        new_low = newInterval[0]
        new_high = newInterval[1]
        for i,inter in enumerate(intervals):
            if inter[1] < new_low:
                output += [inter]
                continue
            if inter[0] > new_high:
                output += [[new_low, new_high]] + intervals[i:]
                inserted = True
                break
            new_low = min(new_low, inter[0])
            new_high = max(new_high, inter[1])
        if not inserted:
            output += [[new_low, new_high]]
        return output

s = Solution()
res = s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8])
print(res)