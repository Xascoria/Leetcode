from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        output = max(nums)
        for i in nums:
            cur_sum += i
            if cur_sum < 0:
                cur_sum = 0
            else:
                output = max(output, cur_sum)

        return output