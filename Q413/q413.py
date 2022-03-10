from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        current_count = 0
        output = 0
        for i in range( len(nums)-2 ):
            if nums[i] - nums[i+1] == nums[i+1] - nums[i+2]:
                current_count += 1
            else:
                output += current_count * (current_count+1) // 2
                current_count = 0
        output += current_count * (current_count+1) // 2
        return output


x = Solution()
print( x.numberOfArithmeticSlices([1,2,3,4,5]) )