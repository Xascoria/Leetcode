from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        
        mid = len(nums)//2
        lower = 0 
        upper = len(nums)
        cur_val = nums[mid]
        if nums[0] == nums[-1] == target:
            return [0,len(nums)-1]

        if len(nums) == 1:
            return [-1,-1]

        while cur_val != target:
            if lower+1 == upper:
                return [-1,-1]
            if cur_val < target:
                lower = mid
            else:
                upper = mid
            mid = (lower + upper)//2
            cur_val = nums[mid]

        output = [mid,mid]
        left_lower = lower
        left_upper = mid
        left_mid = (lower + mid)//2
        if nums[left_lower] == target:
            output[0] = left_lower
        else:
            while left_lower + 1 != left_upper:
                if nums[left_mid] == target:
                    left_upper = left_mid
                else:
                    left_lower = left_mid
                left_mid = (left_lower + left_upper)//2
            output[0] = left_upper
        
        right_lower = mid
        right_upper = upper
        right_mid = (right_lower + right_upper)//2
        if right_upper < len(nums) and nums[right_upper] == target:
            output[1] = right_upper
        else:
            while right_lower + 1 != right_upper:
                if nums[right_mid] == target:
                    right_lower = right_mid
                else:
                    right_upper = right_mid
                right_mid = (right_lower + right_upper)//2
            output[1] = right_lower
        return output