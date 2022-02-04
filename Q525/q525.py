from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        output = 0
        cur_val = 0
        d = {0:-1}
        for i,j in enumerate(nums):
            if j == 0:
                cur_val += 1
            else:
                cur_val -= 1
            if cur_val in d:
                output = max(output, i-d[cur_val])
            else:
                d[cur_val] = i
        return output
