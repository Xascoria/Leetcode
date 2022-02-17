from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out = [0] * len(nums)
        for i,j in enumerate(nums):
            out[i] = out[i-1] + j
        return out