from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 1 and nums[0] >= target:
            return 1

        cur_sum = nums[0]
        cur_start = 0
        cur_end = 1
        subarray_length = float("inf")
        while cur_end < len(nums):
            while cur_sum < target:
                if cur_end == len(nums):
                    break
                cur_sum += nums[cur_end]
                cur_end += 1
            while cur_sum >= target:
                subarray_length = min(subarray_length, cur_end - cur_start)
                cur_sum -= nums[cur_start]
                cur_start += 1
                if cur_start == cur_end:
                    cur_end += 1
                    if cur_end == len(nums) or cur_end == len(nums)+1:
                        break
                    cur_sum = nums[cur_start]
            #if cur_sum >= target:
            #    cur_sum -= nums[cur_start]
            #    cur_start += 1
                # if cur_start == cur_end:
                #     return 1
        if subarray_length == float("inf"):
            return 0
        return subarray_length

x = Solution()
print( x.minSubArrayLen(7, [1,1,1,1,7]) )