from typing import List

from math import gcd
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0: return 
        for i in range(gcd(k, len(nums))):
            start_index = (i+k)% len(nums)
            stored_val = nums[i]
            nums[start_index], stored_val = stored_val, nums[start_index]
            while start_index != i:
                start_index = (start_index+k)% len(nums)
                nums[start_index], stored_val = stored_val, nums[start_index]

x = Solution()
lst = [1,2,3,4,5,6]
x.rotate(lst, 4)
print(lst)