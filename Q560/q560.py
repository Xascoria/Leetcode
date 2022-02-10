from typing import List

## Sliding window DOES NOT WORK, there are negative numbers
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ptr1 = 0
        ptr2 = 1
        output = 0
        while ptr1 < len(nums):
            if sum(nums[ptr1:ptr2]) == k:
                output += 1
                if ptr2 < len(nums):
                    ptr2 += 1
                else:
                    ptr1 += 1
            elif sum(nums[ptr1:ptr2]) < k:
                if ptr2 < len(nums):
                    ptr2 += 1
                else:
                    ptr1 += 1
            else:
                ptr1 += 1
            if ptr1 >= ptr2:
                ptr2 = ptr1 + 1
            print(ptr1, ptr2)
            print(nums[ptr1: ptr2])
        return output

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        accu_d = {0: 1}
        accu_sum = 0
        output = 0
        for i in nums:
            accu_sum += i
            if accu_sum - k in accu_d:
                output += accu_d[accu_sum - k]
            accu_d[accu_sum] = accu_d.get(accu_sum, 0) + 1
        return output

x = Solution()
print(  x.subarraySum([1,-1,0],0) )