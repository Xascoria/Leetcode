from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= k*2:
            return [-1] * len(nums)

        output = [-1] * k 
        run_val = 0
        for i in range(k*2+1):
            run_val += nums[i]
        for i in range(len(nums) - 2*k):
            output.append(run_val// (2*k+1))
            if i+2*k+1 < len(nums):
                run_val += -nums[i] + nums[i+2*k+1]
        output += [-1] * k
        return output


x = Solution()
print( x.getAverages([7,4,3,9,1,8,5,2,6], k = 3) )