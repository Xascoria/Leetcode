from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr_left = [nums[0]] * len(nums)
        for i in range(1,len(arr_left)):
            arr_left[i] = arr_left[i-1] * nums[i]
        arr_left = [1]+arr_left+[1]
        arr_right = [nums[-1]] * len(nums)
        for i in range(len(arr_right)-2,-1,-1):
            arr_right[i] = arr_right[i+1] * nums[i]
        arr_right = [1]+arr_right+[1]
        return [arr_left[i] * arr_right[i+2] for i in range(len(nums))]
    
x = Solution()
print( x.productExceptSelf([1,2,3,4]) )