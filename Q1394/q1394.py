from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = {}
        for i in arr:
            d[i] = d.get(i,0) + 1

        output = -1
        for i in d:
            if i==d[i]:
                output = max(output, i)
        return output