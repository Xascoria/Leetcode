from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        ptr1 = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[ptr1] = nums[i]
                ptr1 += 1
        return ptr1