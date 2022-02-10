from typing import List

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = {}
        for i in arr:
            d[i] = d.get(i, 0) + 1
        accu_sum = 0
        output = 0
        for i in sorted(d.values(), reverse=1):
            accu_sum += i
            output += 1
            if accu_sum >= len(arr) // 2:
                return output
