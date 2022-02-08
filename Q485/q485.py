from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        out = 0
        for i in nums:
            if i:
                count += 1
                out = max(out, count)
            else:
                count = 0
        return out