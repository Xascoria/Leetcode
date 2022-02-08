from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = [0] * len(nums)

        for i in range(1, len(arr)):
            val = nums[i]
            arr[i] = max([arr[j] for j in range(i) if nums[j] < val] + [0]) + 1
        return max(arr)