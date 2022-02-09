from typing import List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k == 0:
            d = {}
            for i in nums:
                d[i] = d.get(i, 0) + 1
            return sum(d[i] > 1 for i in d)
        a = set(nums)
        output = 0
        for i in a:
            if i+k in a:
                output += 1
        return output
