from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0: return 0
        middle = len(nums)//2
        mid_val = nums[middle]
        higher_border = len(nums)
        lower_border = 0
        
        while mid_val != target and lower_border+1 != higher_border:
            if target < mid_val:
                higher_border = middle
            else:
                lower_border = middle
            middle = (lower_border+higher_border)//2
            mid_val = nums[middle]
        if mid_val == target:
            return middle
        elif nums[lower_border] < target:
            return lower_border+1
        return lower_border

x = Solution()
print( x.searchInsert([2],0) )

        
        