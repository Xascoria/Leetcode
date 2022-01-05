from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) < 3: return nums.index(max(nums))
        mid = len(nums)//2
        top = len(nums)
        bottom = 0
        while True:
            if mid == 0 or mid == len(nums)-1:
                return mid
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            if nums[mid] < nums[mid+1]:
                bottom = mid
            else:
                top = mid
            mid = (bottom+top)//2

x = Solution()
print( x.findPeakElement([6,5,4,3,2,3,2]) )