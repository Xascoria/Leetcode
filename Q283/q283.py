from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_ptr = 0
        while nums[zero_ptr] != 0:
            zero_ptr += 1
            if zero_ptr == len(nums):
                return 

        non_zero_ptr = zero_ptr
        while nums[non_zero_ptr] == 0:
            non_zero_ptr += 1
            if non_zero_ptr == len(nums):
                return


        while non_zero_ptr != len(nums):
            nums[zero_ptr], nums[non_zero_ptr] = nums[non_zero_ptr], nums[zero_ptr]
            while nums[zero_ptr] != 0:
                zero_ptr += 1
                if zero_ptr == len(nums):
                    return
            while nums[non_zero_ptr] == 0:
                non_zero_ptr += 1
                if non_zero_ptr == len(nums):
                    return

x = Solution()
k = [1,0]
print( x.moveZeroes(k) )
print(k)