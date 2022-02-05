from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        arr = [pivot] * len(nums)
        ptr = 0
        ptr2 = len(nums)-1
        for i in nums:
            if i < pivot:
                arr[ptr] = i
                ptr += 1
        for i in nums[::-1]:
            if i > pivot:
                arr[ptr2] = i
                ptr2 -= 1
        return arr
        

x = Solution()
print( x.pivotArray([19,15,12,-14,8,-7,-11], -7) )