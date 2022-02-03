from typing import List

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        nums.sort()
        if len(nums) == 1:
            return nums
        output = []
        if nums[1] - nums[0] > 1:
            output.append(nums[0])
        if nums[-1] - nums[-2] > 1:
            output.append(nums[-1])
        for i in range(1, len(nums)-1):
            if nums[i] - nums[i-1] > 1 and nums[i+1] - nums[i] > 1:
                output.append(nums[i])
        return output