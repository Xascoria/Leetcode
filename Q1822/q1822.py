from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        cur_sign = 1
        for i in nums:
            if i == 0:
                return 0

            if i < 0:
                cur_sign = (0, -1, 1)[cur_sign]
        return cur_sign